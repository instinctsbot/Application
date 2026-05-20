from sqlalchemy import (Column, Integer, ForeignKey, DateTime)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Inventory(Base):
    __tablename__ = "Inventory"

    id = Column(Integer, ForeignKey=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    stock_remaining = Column(Integer, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    product = relationship('Product')
