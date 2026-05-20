from sqlalchemy.orm import Session
from app.db.models.store import Store
from app.schemas.store import StoreCreate

class StoreRepository:
    @staticmethod
    def create_store(db: Session, payload: StoreCreate):
        store = Store(
            Name=payload.name,
            shopify_domain=payload.shopify_domain,
            access_token=payload.access_token,
        )
        db.add(store)
        db.commit()
        db.refresh(store)

        return store
    
    @staticmethod
    def get_Store_by_id(db: Session, store_id: int):
        return db.query(Store).filter(Store.id == store_id).first()

    @staticmethod
    def get_all_stores(db : Session):
        return db.query(Store).all()