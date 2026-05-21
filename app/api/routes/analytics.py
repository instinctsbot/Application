from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.analytics.sales_analyzer import SalesAnalyzer


router = APIRouter(prefix="/analytics")


@router.get("/{store_id}/summary")
def analytics_summary(
    store_id: int,
    db: Session = Depends(get_db),
):
    revenue = SalesAnalyzer.calculate_total_revenue(
        db,
        store_id,
    )

    orders = SalesAnalyzer.total_orders(
        db,
        store_id,
    )

    return {
        "revenue": revenue,
        "orders": orders,
    }