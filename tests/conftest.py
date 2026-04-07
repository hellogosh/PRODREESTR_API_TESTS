import sys
from pathlib import Path
import pytest
import uuid
from src.api_client import ApiClient
from src.models.section import Section
from src.models.product_type import ProductType
from src.utils.helpers import generate_unique_name

sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def unique_name():
    return generate_unique_name()

@pytest.fixture
def section(api_client, unique_name):
    """Создаёт раздел и удаляет его после теста."""
    payload = {"name": unique_name}
    resp = api_client.post("/api/sections", json=payload)
    assert resp.status_code == 200, f"Failed to create section: {resp.text}"
    section_data = resp.json()
    yield Section(**section_data)
    api_client.delete(f"/api/sections/{section_data['id']}")

@pytest.fixture
def product_type(api_client, section, unique_name):
    """Создаёт тип в разделе и удаляет его после теста."""
    payload = {
        "name": unique_name,
        "localizedName": unique_name
    }
    resp = api_client.post("/api/producttypes", params={"sectionId": section.id}, json=payload)
    assert resp.status_code == 200, f"Failed to create product type: {resp.text}"
    type_data = resp.json()
    yield ProductType(**type_data)
    api_client.delete(f"/api/producttypes/{type_data['id']}")