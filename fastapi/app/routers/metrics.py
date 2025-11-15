from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/")
async def metrics():
    """
    Metrics probe endpoint for Prometheus
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


__all__ = ["router"]
