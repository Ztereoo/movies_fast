from httpx import AsyncClient

async def test_registration(ac: AsyncClient):
    response = await ac.post("/auth/registration", json={
        "name" : "Sharik",
        "email": "kot@pes.com",
        "password" : "kotopes",
    })
    assert response.status_code == 200
