from django.http import HttpRequest
from ninja import Router

from app.schemas import HelloWorldOutSchema

router = Router()


@router.get("/hello_world", response={200: HelloWorldOutSchema}, url_name="hello_world")
def hello_world(request: HttpRequest):
    return 200, HelloWorldOutSchema(response_text="Hello, World")


@router.get("/ping", url_name="ping")
def ping(request: HttpRequest):
    return {"message": "pong"}
