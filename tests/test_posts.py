import pytest


@pytest.mark.smoke
@pytest.mark.parametrize("post_id", [1, 2, 50, 100])
def test_get_post(session, base_url, post_id):
    r = session.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == 200
    assert r.json()["id"] == post_id


def test_get_posts(session, base_url):
    r = session.get(f"{base_url}/posts")
    assert r.status_code == 200
    assert len(r.json()) > 0


def test_create_post(session, base_url):
    payload = {"title": "hello", "body": "world", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["title"] == payload["title"]


@pytest.mark.negative
def test_get_missing_post_returns_404(session, base_url):
    r = session.get(f"{base_url}/posts/99999")
    assert r.status_code == 404


def test_post_has_expected_fields(session, base_url):
    post = session.get(f"{base_url}/posts/1").json()
    expected = {"userId", "id", "title", "body"}
    assert expected <= post.keys()
    assert {k: post[k] for k in ("id", "userId")} == {"id": 1, "userId": 1}
