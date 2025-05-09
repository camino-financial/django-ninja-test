from ninja import NinjaAPI, Swagger
from app.api import router


api = NinjaAPI(
    title="Django Ninja API",
    version="1.0.0",
    urls_namespace="api",
    docs=Swagger(),
)

api.add_router("", router)
