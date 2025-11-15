from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health():
    """
    Health probe endpoint for kubernetes
    """
    # TODO: Implement
    return {"status": "ok"}


__all__ = ["router"]
