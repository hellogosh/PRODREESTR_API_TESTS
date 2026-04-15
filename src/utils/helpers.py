import uuid
from faker import Faker

fake = Faker('ru_RU')

def generate_unique_name(prefix: str = "test") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def random_product_name() -> str:
    return f"Продукт {fake.word()} {fake.random_int(1, 999)}"

def random_product_code() -> str:
    return f"PRD-{fake.random_int(1000,9999)}"

def random_description() -> str:
    return fake.sentence(nb_words=10)

def random_url() -> str:
    return fake.url()

def random_email() -> str:
    return fake.email()

def random_phone() -> str:
    return fake.phone_number()

