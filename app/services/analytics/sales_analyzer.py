from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models.order import Order


class SalesAnalyzer:

    @staticmethod
    def calculate_total_revenue(
        db: Session,
        store_id: int,
    ):
        revenue = db.query(
            func.sum(Order.total_price)
        ).filter(
            Order.store_id == store_id
        ).scalar()

        return revenue or 0

    @staticmethod
    def total_orders(
        db: Session,
        store_id: int,
    ):
        count = db.query(Order).filter(
            Order.store_id == store_id
        ).count()

        return count