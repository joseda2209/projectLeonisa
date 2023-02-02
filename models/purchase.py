from config.database import Base
from sqlalchemy import Column, Uuid, Double, DateTime
from sqlalchemy.orm import relationship
import uuid

class Purchase(Base):
    __tablename__ = 'purchase'
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    value = Column(Double)
    date = Column(DateTime)

    details = relationship("PurchaseDetail", back_populates='purchase')