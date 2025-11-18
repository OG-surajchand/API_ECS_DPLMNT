from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from typing import Optional, List


class Item(BaseModel):
    id: UUID
    name: str = Field(..., example="Widget")
    description: Optional[str] = Field(None, example="A useful widget")
    price: float = Field(..., gt=0, example=9.99)
    tags: List[str] = Field(default_factory=list)
