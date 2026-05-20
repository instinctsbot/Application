from pydantic import BaseModel

class StoreCreate(BaseModel):
    name : str
    shopify_domain : str
    access_token : str

class StoreResponse(BaseModel):
    id: int 
    name : str
    shopify_domain : str

    class Config:
        from_attributes = True
