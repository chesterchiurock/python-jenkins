from app import *

def testHome():
    response = app.test_client().get('/')
    assert b"ok" in response.data
    assert response.status_code == 200