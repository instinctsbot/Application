from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.store import (StoreCreate, StoreResponse)

from app.repositories.store_repo import StoreRepository
from app.services.shopify.sync_service import ShopifySyncService

router = APIRouter(prefix="/store")

@router.post("/connect", response_model=StoreResponse)
def connect_store(
    payload : StoreCreate,
    db : Session = Depends(get_db)
):
    store = StoreRepository.create_store(db, payload)
    return store

@router.post("/{store_id}/sync")
def sync_store(
    store_id : int,
    db : Session = Depends(get_db),
):
    store = StoreRepository.get_store_by_id(db, store_id)
    sync_service = ShopifySyncService(db, store)

    orders_synced = sync_service.sync_orders()
    product_synced = sync_service.sync_products()

    return  {
        "orders_synced" : orders_synced,
        "products_synced" : product_synced,
    }