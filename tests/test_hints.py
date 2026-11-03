import requests

from utils.checks import build_post, find_post


def test_find_post(session: requests.Session, base_url: str) -> None:
    posts = session.get(f"{base_url}/posts").json()
    post = find_post(posts, 3)
    assert post is not None
    assert post["id"] == 3


def test_build_post() -> None:
    payload = build_post("hello", "world")
    assert payload["userId"] == 1