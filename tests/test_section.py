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

def test_update_section(api_client, unique_name):
    #create
    create_payload = {"name": unique_name}
    create_resp = api_client.post("/api/sections", json=create_payload)
    assert create_resp.status_code == 200
    section = create_resp.json()
    section_id = section['id']

    #update
    new_name = f'update_{unique_name}'
    update_payload = {'id': section_id, 'name': new_name}
    update_resp = api_client.put("/api/sections", json=update_payload)
    assert update_resp.status_code == 200
    updated = update_resp.json()
    assert updated['name'] == new_name

    #cleanup
    api_client.delete(f'/api/sections/{section_id}')
    assert api_client.get(f"/api/sections/{section_id}").status_code == 405

