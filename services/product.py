from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductSchema

class ProductService():
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_products(self):
        return self.db.query(Product).all()

    def get_one_product(self, id):
        return self.db.query(Product).filter(Product.id == id).first()

    def create_product(self, product: ProductSchema):
        product_model = Product(**product.dict())
        self.db.add(product_model)
        self.db.commit()
        self.db.refresh(product_model)
        return product_model