from sqlalchemy.orm import Session
from app.db.models.product import Product

class ProductRepository:

    @staticmethod
    def create_product(
        db : Session,
        store_id : int,
        shopify_product_id : str,
        name : str,
        category : str,
        price : float,
    ):
        existing = db.query(Product).filter(Product.shopify_product_id == shopify_product_id).first()

        if existing:
            return existing
        
        product = Product(
            store_id=store_id,
            shopify_product_id=shopify_product_id,
            name=name,
            category=category,
            price=price,
        )

        db.add(product)
        db.commit()
        db.refresh()

        return product