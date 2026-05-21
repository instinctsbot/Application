from sqlalchemy.orm import Session

from app.db.models.inventory import Inventory


class InventoryAnalyzer:

    @staticmethod
    def low_stock_products(
        db: Session,
        threshold: int = 10,
    ):
        return db.query(Inventory).filter(
            Inventory.stock_remaining < threshold
        ).all()