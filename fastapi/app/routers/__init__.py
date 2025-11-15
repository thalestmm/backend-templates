from fastapi import APIRouter

from app.routers.api import router as api_router
from app.routers.health import router as health_router
from app.routers.metrics import router as metrics_router

router = APIRouter(prefix="")

router.include_router(api_router)
router.include_router(health_router)
router.include_router(metrics_router)

__all__ = ["router"]
