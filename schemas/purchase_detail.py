from typing import Optional
from pydantic import BaseModel, Field
import uuid

class PurchaseDetailSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    quantity: int = Field(
        ...,
        title='Quantity',
        description='Quantity of the product to Purchase',
        ge=1,
        example=2,
    )
    id_purchase: Optional[uuid.UUID] = Field(
        default=None,
        title='Id Purchase',
        description='Id of Purchase associated'
    )
    id_product: uuid.UUID = Field(
        ...,
        title='Id Product',
        description='Id of product to purchase',
    )

    class Config:
        orm_mode = True
