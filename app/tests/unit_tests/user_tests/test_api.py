from httpx import AsyncClient
import pytest

@pytest.mark.parametrize("name, email, password, status_code",[
    ("Sharik","kot@pes.com","kotopes",200)
])
async def test_registration(name, email, password, status_code,ac: AsyncClient):
    response = await ac.post("/auth/registration", json={
        "name": name,
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code
