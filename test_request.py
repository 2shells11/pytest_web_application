import pytest
import json
import requests
import jsonpath

def test_setup(setup):
    print("Executing")

def test_get_request():
    
    url = "http://127.0.0.1:5000/books"
    response = requests.get(url)
    print(response)
    print(response.text)
    json_response = json.loads(response.text)
    print(json_response)


def test_get_request_by_id(get_request_by_id_fixture):
    id1 = input("enter id")
    #url1= "http://127.0.0.1:5000/book/"+id1
    response1= get_request_by_id_fixture(id1)
    print(response1)
    assert response1.status_code == 200

def test_post_request():
    url = "http://127.0.0.1:5000/books"
    response_post = requests.post(url)
    print(response_post)
    assert response_post.status_code == 201


def test_put_request(put_fixture):
    id2 = input("enter id")
    #url2= "http://127.0.0.1:5000/book/"+id2
    response_putt= put_fixture(id2)
    print(response_putt)
    assert response_putt.status_code == 200

def test_delete_request():
    id3 = input("enter id")
    url3= "http://127.0.0.1:5000/book/"+id3
    response_del= requests.delete(url3)
    print(response_del)
    assert response_del.status_code == 200