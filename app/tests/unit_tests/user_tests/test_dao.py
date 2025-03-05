import pytest

from app.users.dao import UserDao


@pytest.mark.parametrize(
    "user_id,email,exists",
    [
        (1, "alice@example.com", True),
        (2, "bob@example.com", True),
        (33, "smth", False),
    ],
)
async def test_find_user_by_id(user_id, email, exists):
    user = await UserDao.find_by_id(user_id)
    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user
