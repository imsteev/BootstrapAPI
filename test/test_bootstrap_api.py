import requests

def test_server_ok():
    res = requests.get('http://localhost:8888')
    assert res.status_code == 200

if __name__ == "__main__":
    test_server_ok()
    print("Tests passed!")