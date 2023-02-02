import datetime, uuid
from typing import List,Optional
from pydantic import BaseModel,Field
from schemas.purchase_detail import PurchaseDetailSchema

class PurchaseSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    value: float = Field(
        default=0,
        title='Value',
        description='Total Value of Purchase',
        ge=0
    )
    date: datetime.datetime = Field(
        default=None,
        title='Date',
        description='Date of purchase'
    )
    details: List[PurchaseDetailSchema] = []

    class Config:
        orm_mode = True
    