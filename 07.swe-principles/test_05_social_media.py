# poetry run pytest

from collections import Counter

import pytest
from text_analyzer import SocialMedia

test_post = "learning #python & #rstats is awesome! thanks @datacamp!"
sm_post = SocialMedia(test_post)


# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({"python": 1, "rstats": 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts


# Fixture (runs before tests)
@pytest.fixture
def social_media_post():
    return SocialMedia("learning #python & #rstats!")


# Test using the fixture
def test_hashtags(social_media_post):
    assert social_media_post.hashtag_counts["python"] == 1
    assert "rstats" in social_media_post.hashtag_counts


# Parameterized test
@pytest.mark.parametrize(
    "text,expected_count,expected_hashtags",
    [
        ("#python", 1, {"python": 1}),
        ("no hashtags", 0, {}),
        ("#python #python", 1, {"python": 2}),  # Same hashtag counts are combined
        ("#python #rstats", 2, {"python": 1, "rstats": 1}),
    ],
)
def test_hashtag_counting(text, expected_count, expected_hashtags):
    post = SocialMedia(text)
    assert len(post.hashtag_counts) == expected_count
    assert post.hashtag_counts == Counter(expected_hashtags)
