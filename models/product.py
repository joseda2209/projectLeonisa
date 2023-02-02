from config.database import Base
from sqlalchemy import Column, String, Double, Uuid, Integer
import uuid

class Product(Base):
    __tablename__ = 'product'
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False , unique=True)
    description = Column(String(255))
    value = Column(Double, nullable=False)
    stock = Column(Integer, default=0)