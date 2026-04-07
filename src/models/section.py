from pydantic import BaseModel
from typing import Optional, List

class ProductTypeRef(BaseModel):
    id: int
    name: str

class Section(BaseModel):
    id: Optional[int] = None
    name: str
    translitName: Optional[str] = None
    productTypes: Optional[List[ProductTypeRef]] = []