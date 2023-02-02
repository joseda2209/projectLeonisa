from typing import Optional
from pydantic import BaseModel, Field
import uuid

class ProductSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str = Field(
        ...,
        title='Name',
        description='Name of the product',
        min_length=5,
        max_length=100,
        example="Mouse Rog Chackram X"
    )
    description: Optional[str] = Field(
        default=None,
        title='Description',
        description='Short description of the product',
        min_length=10,
        max_length=250,
        example='Mouse ergonomico de la marca Republic of Gamers'
    )
    value: float = Field(
        ...,
        title='Value',
        description='Unit value of the product',
        example= 400000
    )
    stock: int = Field(
        ...,
        title='stock',
        description='Number of the units in stock of the product',
        ge=0,
        example= 10
    )