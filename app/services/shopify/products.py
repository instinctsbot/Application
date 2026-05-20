from app.services.shopify.client import ShopifyClient

class ShopifyProductsService:
    def __init__(self, client : ShopifyClient):
        self.client = client
    
    def fetch_products(self):
        response = self.client.get("products.json")

        return response.get("products", [])