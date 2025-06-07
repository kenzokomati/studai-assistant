import logging
import threading
from app.context import request_id_contextvar, trace_id_contextvar

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        request_id = request_id_contextvar.get()
        record.request_id = request_id if request_id else "no-request-id"
        trace_id = trace_id_contextvar.get()
        record.trace_id = trace_id if trace_id else "no-trace-id"
        record.threadName = threading.current_thread().name
        return True

logger = logging.getLogger("studai-assistant-logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)5s] [%(threadName)s] "
    "[service=studai-assistant] [request_id=%(request_id)s] [trace_id=%(trace_id)s] "
    "[logger=%(name)s] | %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(RequestIdFilter())

logger.addHandler(handler)
