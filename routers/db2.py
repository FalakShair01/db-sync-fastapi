from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models import subscription_db2
from schemas import schema

router = APIRouter(tags=['Db2 Test Routes'])

# end-point to get all subscription from db2 for test
@router.get("/db2", response_model=list[schema.Subscription])
async def get_all_subscriptions_from_db2(db: Session = Depends(get_db)):
    subscriptions = db.query(subscription_db2.Subscription2).all()
    return subscriptions

# end-point to create test subscription in db2
@router.post("/create-db2", response_model=schema.Subscription)
async def create_subscription_in_db2(subscription: schema.Subscription, db: Session = Depends(get_db)):
    subscription_data = subscription_db2.Subscription2(email=subscription.email, active=subscription.active)
    db.add(subscription_data)
    db.commit()
    db.refresh(subscription_data)
    return subscription_data

