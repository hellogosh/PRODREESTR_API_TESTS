from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    login: str
    phone: Optional[str] = None
    email: Optional[str] = None
    telegram: Optional[str] = None

class SupportType(BaseModel):
    id: int
    name: str
    localizedName: str
    wikiUrl: Optional[str] = None

class ProductStatus(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str
    productCode: str
    owner: Optional[User] = None
    externalSupportEmployee: Optional[User] = None
    status: Optional[ProductStatus] = None
    supportType: Optional[SupportType] = None
    jiraUrl: Optional[str] = None
    wikiUrl: Optional[str] = None
    description: Optional[str] = None
    repositoryCodes: Optional[str] = None
