def test_get_products(api_client):
    resp = api_client.get("/api/products")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)