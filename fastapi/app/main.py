import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.middleware import MetricsMiddleware
from app.routers import router as main_router

logger = logging.getLogger("__name__")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting FastAPI application...")

    yield

    logger.info("Shutting down FastAPI application...")


app: FastAPI = FastAPI(
    title="FastAPI Template",
    version="0.1.0",
    description="FastAPI template for backend applications",
    lifespan=lifespan,
)

# Include middleware
app.add_middleware(MetricsMiddleware)

# Include custom routers
app.include_router(main_router)


@app.get("/")
async def root():
    logger.debug("Root endpoint called")

    if not settings.is_production:
        logger.debug("Redirecting to documentation")
        return RedirectResponse(url="/docs")

    return {"status": "ok"}
