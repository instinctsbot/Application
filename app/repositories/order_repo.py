from sqlalchemy.orm import Session
from app.db.models.order import Order

class OrderRepository:

    @staticmethod
    def create_order(
        db : Session,
        store_id : int,
        shopify_order_id : str,
        total_price : float,
        currency : str,
        status : str,
    ):
        
        existing = db.query(Order).filter(Order.shopify_order_id == shopify_order_id).first()

        if existing:
            return existing
        
        order = Order(
            store_id=store_id,
            shopify_order_id=shopify_order_id,
            total_price=total_price,
            currency=currency,
            status=status,
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        return order
    
    @staticmethod
    def get_orders_by_store(db : Session, store_id : int):
        return db.query(Order).filter(Order.store_id == store_id).all()