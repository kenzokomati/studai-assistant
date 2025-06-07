from starlette.middleware.base import BaseHTTPMiddleware
import time
import uuid
from app.logger import logger
from app.context import request_id_contextvar, trace_id_contextvar

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        trace_id = request.headers.get("X-B3-TraceId", str(uuid.uuid4()))

        request_id_contextvar.set(request_id)
        trace_id_contextvar.set(trace_id)

        start_time = time.time()
        response = await call_next(request)
        process_time = int((time.time() - start_time) * 1000)

        # Set extra fields for the logger
        logger.info(
            f"{request.method} {request.url.path} - {response.status_code} - {process_time}ms",
            extra={
                "method": request.method,
                "path": request.url.path
            }
        )

        return response
