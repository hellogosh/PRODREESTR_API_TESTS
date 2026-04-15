from src.utils.payload_factory import create_product_payload
from src.models.product import Product

def test_get_products(api_client):
    resp = api_client.get("/api/products")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    for product in data:
        print(f"ID: {product['id']}, Name: {product['name']}")


def test_create_product(api_client, section, product_type, unique_name, statuses, support_types, contacts):
    # Получаем справочные данные (статус, тип поддержки, внешний СЭ)
    status = statuses[0]
    support_type = support_types[0]
    external_se = contacts[0]

    payload = create_product_payload(product_type.id, section.name, unique_name, status, support_type, external_se)

    resp = api_client.post("/api/products", json=payload)
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}, body: {resp.text}"

    data = resp.json()
    product_data = data["products"][0]

    product = Product(**product_data)

    assert product.name == f"product_{unique_name}"
    assert product.productCode == f"code_{unique_name}"
    assert product.status.id == status["id"]
    assert product.supportType.id == support_type["id"]
    assert product.externalSupportEmployee.id == external_se["id"]

    api_client.delete(f"/api/products/{product.id}")

def test_update_product(api_client, section, product_type, unique_name, statuses, support_types, contacts):
    # 1. Получаем справочные данные
    status = statuses[0]
    support_type = support_types[0]
    external_se = contacts[0]

    # 2. Создаём продукт через POST
    create_payload = create_product_payload(
        product_type.id, section.name, unique_name,
        status, support_type, external_se
    )
    create_resp = api_client.post("/api/products", json=create_payload)
    assert create_resp.status_code == 200
    product_data = create_resp.json()["products"][0]
    product = Product(**product_data)
    product_id = product.id

    # 3. Формируем payload для обновления
    # Копируем исходный payload, добавляем id продукта и меняем name/productCode
    update_payload = create_payload.copy()
    update_payload["products"][0]["id"] = product_id
    new_name = f"updated_{unique_name}"
    new_code = f"updated_code_{unique_name}"
    update_payload["products"][0]["name"] = new_name
    update_payload["products"][0]["productCode"] = new_code

    # 4. Отправляем PUT запрос
    update_resp = api_client.put("/api/products", json=update_payload)
    assert update_resp.status_code == 200, f"Expected 200, got {update_resp.status_code}, body: {update_resp.text}"
    updated_product_data = update_resp.json()["products"][0]
    updated_product = Product(**updated_product_data)

    # 5. Проверяем, что поля обновились
    assert updated_product.id == product_id
    assert updated_product.name == new_name
    assert updated_product.productCode == new_code
    # Проверяем, что неизменные поля остались прежними (статус, поддержка, внешний СЭ)
    assert updated_product.status.id == status["id"]
    assert updated_product.supportType.id == support_type["id"]
    assert updated_product.externalSupportEmployee.id == external_se["id"]

    # 6. Очистка
    api_client.delete(f"/api/products/{product_id}")






