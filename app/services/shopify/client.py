import requests

class ShopifyClient:
    def __init__(self, shopify_domain : str, access_token : str):
        self.base_url = f"https://{shopify_domain}/admin/api/2024-01"

        self.headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json",
        }

    def get(self, endpoint : str, params=None):
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params
        )

        response.raise_for_status()

        return response.json()