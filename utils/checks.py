from typing import Any


def build_post(title: str, body: str, user_id: int = 1) -> dict[str, Any]:
    return {"title": title, "body": body, "userId": user_id}


def find_post(posts: list[dict[str, Any]], post_id: int) -> dict[str, Any] | None:
    for post in posts:
        if post["id"] == post_id:
            return post
    return None