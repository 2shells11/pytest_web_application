import pytest
import requests

@pytest.fixture(scope="session")
def setup():
    print("Doing setup")
    res=requests.get("http://127.0.0.1:5000/books")
    assert res.status_code == 200
    print("application is running")
    yield
    print("\nDoing teardown")
            



@pytest.fixture(scope="function")
def put_fixture():
    def put_request(id2):
        url2= "http://127.0.0.1:5000/book/"+id2
        response_put= requests.put(url2)

        return response_put
    return put_request

@pytest.fixture(scope="function")
def get_request_by_id_fixture():
    def get_by_id_request(id1):
        url1= "http://127.0.0.1:5000/book/"+id1
        response_get_by_id= requests.get(url1)
        return response_get_by_id
    return get_by_id_request
