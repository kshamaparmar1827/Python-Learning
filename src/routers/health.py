from src.routers.router import v1_router


@v1_router.get("/health")
def health_check():
    return {"status": "ok"}
