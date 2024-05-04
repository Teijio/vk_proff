from httpx import AsyncClient


async def test_user_create(async_client: AsyncClient):
    response = await async_client.post(
        "/user/user_create",
        json={
            "login": "user@example.com",
            "password": "stringstri",
            "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "env": "prod",
            "domain": "canary",
        },
    )

    assert response.status_code == 200
