from sqlalchemy import (Column, Integer, String, Float, ForeignKey, DateTime)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    shopify_order_id = Column(String, unique=True, nullable=False)
    total_price = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    store = relationship("Store")
    