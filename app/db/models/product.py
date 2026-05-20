from sqlalchemy import (Column, Integer, String, Float, ForeignKey, DateTime)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    shopify_product_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    store = relationship("Store")