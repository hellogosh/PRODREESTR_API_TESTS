from src.api_client import ApiClient

def test_get_sections(api_client):
    response = api_client.get("/api/sections")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print(f"Got {len(data)} sections")

def test_create_section(api_client, unique_name):
    payload = {"name": unique_name}
    response = api_client.post("/api/sections", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == unique_name
    # clean up
    api_client.delete(f"/api/sections/{data['id']}")
