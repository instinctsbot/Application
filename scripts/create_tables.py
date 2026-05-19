from app.db.base import Base
from app.db.session import engine

from app.db.models.store import Store
from app.db.models.order import Order
from app.db.models.product import Product
from app.db.models.inventory import Inventory

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Done")