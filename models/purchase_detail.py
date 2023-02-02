from config.database import Base
from sqlalchemy import Column, ForeignKey, Uuid, Integer, DateTime
from sqlalchemy.orm import relationship
import uuid

class PurchaseDetail(Base):
    __tablename__ = 'purchase_detail'
    id = Column(Uuid(as_uuid=True),primary_key=True, default=uuid.uuid4)
    quantity = Column(Integer, default=1, nullable=False)
    id_purchase = Column(Uuid, ForeignKey('purchase.id'))
    id_product = Column(Uuid, ForeignKey('product.id'))
    
    purchase = relationship('Purchase', back_populates='details')
    product = relationship('Product')
