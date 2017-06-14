def test_index_get(test_client):
    rv = test_client.get('/')
    assert rv.status_code == 200
