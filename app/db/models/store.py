from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.base import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    shopify_domain = Column(String, unique=True, nullable=False)
    access_token = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    