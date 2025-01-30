from httpx import AsyncClient
import pytest


@pytest.mark.parametrize("name, email, password, status_code", [
    ("Sharik", "kot@pes.com", "kotopes", 200),
    ("Sharik", "kot@pes.com", "kotT", 409),
    ("Marik", "abcde", "kotopes", 422),
])
async def test_registration(name, email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/registration", json={
        "name": name,
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200),
    ("test2@test2.com", "test2", 200),
    ("test@test.com", "tedst", 401),
    ("tepst@test.com", "test", 401),
]
                         )
async def test_login(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code
