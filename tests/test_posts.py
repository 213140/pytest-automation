import pytest
import requests 
import conftest

@pytest.mark.smoke
def get_post_test(int: id):
    r = requests.get(conftest.base_url() + "/posts/" + id)
    json = r.json()
    assert r.status_code == 200 and json["id"] == id

def get_posts_test():
    r = requests.post(conftest.base_url() + "/posts")
    json = r.json()
    assert r.status_code == 200
    assert r.json != {}

def post_posts_test(string: json_body):
    r = requests.post(conftest.base_url() + "/posts", json=json_body)
    json = r.json()
    assert r.status_code == 201 and json["id"] == 1