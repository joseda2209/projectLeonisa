import uuid
from sqlalchemy.orm import Session
from models.purchase_detail import PurchaseDetail
from schemas.purchase_detail import PurchaseDetailSchema

class PurchaseDetailService():
    def __init__(self, db: Session) -> None:
        self.db = db

    def save_purchase_details(self, purchase_detail: PurchaseDetailSchema):
        purchase_detail_model = PurchaseDetail(**purchase_detail.dict())
        self.db.add(purchase_detail_model)
        self.db.commit()
        self.db.refresh(purchase_detail_model)
        return purchase_detail_model