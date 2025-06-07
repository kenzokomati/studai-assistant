import contextvars

request_id_contextvar = contextvars.ContextVar("request_id", default=None)
trace_id_contextvar = contextvars.ContextVar("trace_id", default=None)
