from app.reviews.dao import ReviewDao


async def test_add_and_get_review():
    new_review = await ReviewDao.add_item(
        movie_id=3, user_id=5, rating=1, comment="Baddest movie"
    )
    assert new_review.movie_id == 3
    assert new_review.user_id == 5

    test_booking = await ReviewDao.find_by_id(new_review.id)
    assert test_booking is not None
