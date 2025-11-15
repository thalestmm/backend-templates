from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from prometheus_client import Counter
from starlette.requests import Request
from starlette.responses import Response

# <-- Prometheus Metrics -->
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of requests",
    ["app_name", "method", "endpoint", "status_code"],
)

# TODO: With multiple workers, the metrics can be picked up by any of them
# TODO: Find a way to aggregate the results in Prometheus


# <-- Middlewares -->
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)

        REQUEST_COUNT.labels(
            app_name="fastapi-backend",
            method=request.method,
            endpoint=request.url.path,
            status_code=str(response.status_code),
        ).inc()

        return response


__all__ = ["MetricsMiddleware"]
