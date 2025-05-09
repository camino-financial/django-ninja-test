from django.test import Client
from django.urls import reverse


def test_hello_world(client: Client):
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"response_text": "Hello, World"}


def test_not_found(client: Client):
    response = client.get("/not_found")
    assert response.status_code == 404


def test_ping(client: Client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
