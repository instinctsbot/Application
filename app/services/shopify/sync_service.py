from sqlalchemy.orm import Session

from app.db.models.store import Store

from app.repositories.order_repo import OrderRepository
from app.repositories.product_repo import ProductRepository

from app.services.shopify.client import ShopifyClient
from app.services.shopify.orders import ShopifyOrdersService
from app.services.shopify.products import ShopifyProductsService


class ShopifySyncService:

    def __init__(self, db: Session, store: Store):
        self.db = db
        self.store = store

        self.client = ShopifyClient(
            shopify_domain=store.shopify_domain,
            access_token=store.access_token,
        )
    
    def sync_orders(self):
        service = ShopifyOrdersService(self.client)
        
        orders = service.fetch_orders()

        for order in orders:
            OrderRepository.create_order(
                db = self.db,
                store_id = self.store.id,
                shopify_order_id=str(order["id"]),
                total_price=float(order["total_price="]),
                currency=order["currency"],
                status=order["financial_status"],
            )
        
        return len(orders)
    
    def sync_products(self):
        service = ShopifyProductsService(self.client)

        products = service.fetch_products()

        for product in products:
            ProductRepository.create_product(
                db=self.db,
                store_id=self.store.id,
                shopify_product_id=str(product["id"]),
                name=product["title"],
                category=product.get("product_type", "Unknown"),
                price=float(product["variants"][0]["price"])
            )
        return len(products)