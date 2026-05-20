from app.services.shopify.client import ShopifyClient

class ShopifyOrdersService:
    def __init__(self, client : ShopifyClient):
        self.client = client
    
    def fetch_orders(self):
        response = self.client.get("orders.json")

        return response.get("orders", [])