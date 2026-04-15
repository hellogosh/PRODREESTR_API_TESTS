
"""Базовые позитивные сценарии"""
def test_create_product_type(api_client, section, unique_name):
    payload = {
        "name": unique_name,
        "localizedName": unique_name
    }
    resp = api_client.post("/api/producttypes", params={"sectionId": section.id}, json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == unique_name
    api_client.delete(f"/api/producttypes/{data['id']}")

def test_get_product_types_by_section(api_client, section, product_type):
    # product_type уже создан фикстурой в этом разделе
    resp = api_client.get("/api/producttypes", params={"sectionName": section.name})
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert any(t["name"] == product_type.name for t in data)


"""Проверка дублей"""
def test_duplicate_type_in_different_sections(api_client, unique_name):
    # Создаём два раздела
    section1 = api_client.post("/api/sections", json={"name": f"sec1_{unique_name}"}).json()
    section2 = api_client.post("/api/sections", json={"name": f"sec2_{unique_name}"}).json()
    type_name = "common_type"
    # Тип в первом разделе
    resp1 = api_client.post("/api/producttypes", params={"sectionId": section1["id"]}, json={"name": type_name, "localizedName": type_name})
    assert resp1.status_code == 200
    type1_id = resp1.json()["id"]
    # Тип с таким же именем во втором разделе
    resp2 = api_client.post("/api/producttypes", params={"sectionId": section2["id"]}, json={"name": type_name, "localizedName": type_name})
    assert resp2.status_code == 200
    type2_id = resp2.json()["id"]

    # Очистка
    api_client.delete(f"/api/producttypes/{type1_id}")
    api_client.delete(f"/api/producttypes/{type2_id}")
    api_client.delete(f"/api/sections/{section1['id']}")
    api_client.delete(f"/api/sections/{section2['id']}")

def test_duplicate_type_in_same_section(api_client, section, unique_name):
    type_name = unique_name   # уникальное имя для этого теста
    # Создаём первый тип
    payload = {"name": type_name, "localizedName": type_name}
    resp1 = api_client.post("/api/producttypes", params={"sectionId": section.id}, json=payload)
    assert resp1.status_code == 200
    type1_id = resp1.json()["id"]
    # Создаём второй тип с таким же именем в том же разделе
    resp2 = api_client.post("/api/producttypes", params={"sectionId": section.id}, json=payload)
    assert resp2.status_code == 200, f"Duplicate in same section should be allowed, got {resp2.status_code}"
    type2_id = resp2.json()["id"]
    # Убеждаемся, что это разные типы (разные id)
    assert type1_id != type2_id
    # Очистка
    api_client.delete(f"/api/producttypes/{type1_id}")
    api_client.delete(f"/api/producttypes/{type2_id}")

"""Обновление типа"""
def test_update_product_type(api_client, product_type, unique_name):
    new_name = unique_name
    payload = {
        "id": product_type.id,
        "name": new_name,
        "localizedName": product_type.localizedName
    }
    resp = api_client.put("/api/producttypes", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == new_name


"""Удаление типа"""
def test_delete_product_type(api_client, section, product_type):
    resp = api_client.delete(f"/api/producttypes/{product_type.id}")
    assert resp.status_code == 200
    # Проверяем, что тип исчез из списка типов раздела
    resp_list = api_client.get("/api/producttypes", params={"sectionName": section.name})
    assert resp_list.status_code == 200
    data = resp_list.json()
    assert not any(t["id"] == product_type.id for t in data)