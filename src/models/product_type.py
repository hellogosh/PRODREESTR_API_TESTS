from pydantic import BaseModel
from typing import Optional, List

class ProductShort(BaseModel):
    id: int
    name: str

class ProductType(BaseModel):
    id: int
    name: str
    localizedName: Optional[str] = None
    products: Optional[List[ProductShort]] = []

