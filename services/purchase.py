import datetime
from sqlalchemy import func, cast, Date
from sqlalchemy.orm import Session
from models.purchase import Purchase
from schemas.purchase import PurchaseSchema, PurchaseDetailSchema
from services.product import ProductService
from services.purchase_detail import PurchaseDetailService

class PurchaseService():
    def __init__(self, db: Session) -> None:
        self.db = db

    def make_purchase(self, purchase: PurchaseSchema):
        for detail in purchase.details:
            product = ProductService(self.db).get_one_product(detail.id_product)
            purchase.value += (product.value * detail.quantity)
        purchase_model = Purchase(value = purchase.value, date=datetime.datetime.now())
        self.db.add(purchase_model)
        self.db.commit()
        self.db.refresh(purchase_model)
        for detail in purchase.details:
            detail.id_purchase = purchase_model.id
            PurchaseDetailService(self.db).save_purchase_details(detail) 
        return purchase_model

    def get_purchases_by_date(self, start_date: datetime.datetime, final_date: datetime.datetime):
        return self.db.query(cast(Purchase.date, Date), func.sum(Purchase.value) ).filter(Purchase.date >= start_date, Purchase.date <= final_date).group_by(cast(Purchase.date, Date)).all()