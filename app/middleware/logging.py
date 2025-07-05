from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
import time
import uuid
import os

from app.logger import logger
from app.context import request_id_contextvar, trace_id_contextvar

SECURITY_KEY = os.getenv("SECURITY_KEY")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        trace_id = request.headers.get("X-B3-TraceId", str(uuid.uuid4()))

        request_id_contextvar.set(request_id)
        trace_id_contextvar.set(trace_id)

        skip_auth_paths = ["/health", "/docs", "/openapi.json"]
        if request.url.path not in skip_auth_paths:
            auth_header = request.headers.get("authorization")
            if not auth_header:
                return JSONResponse(status_code=401, content={"detail": "Invalid or missing API key"})

            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != "bearer" or parts[1] != SECURITY_KEY:
                return JSONResponse(status_code=403, content={"detail": "Invalid or missing API key"})

        start_time = time.time()
        response = await call_next(request)
        process_time = int((time.time() - start_time) * 1000)

        logger.info(
            f"{request.method} {request.url.path} - {response.status_code} - {process_time}ms",
            extra={
                "method": request.method,
                "path": request.url.path
            }
        )

        return response
