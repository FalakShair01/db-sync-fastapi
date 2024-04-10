from fastapi import Depends
from sqlalchemy.orm import Session
from models.subscription1 import Subscription1
from models.subscription2 import Subscription2
from database import db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Dependency
def get_db():
    db = db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def sync_subscriptions( db_session: Session = Depends(get_db)):
    try:
        # Filter inactive subscriptions from db2
        inactive_subscriptions = db_session.query(Subscription2).filter(Subscription2.status == "inactive").all()
        
        # Check status of inactive subscriptions in db1
        for subscription in inactive_subscriptions:
            email = subscription.email
            status_db1 = get_subscription_status_from_db1(db_session, email)
            if status_db1 == "active":
                # Update entry in db2
                subscription.status = "active"
                db_session.commit()
    except Exception as e:
        print(str(e))

def get_subscription_status_from_db1(db_session: Session, email: str) -> str:
    subscription = db_session.query(Subscription1).filter(Subscription1.email == email).first()
    return subscription.status if subscription else "inactive"


async def schedule_sync_task():
    # Schedule sync task to run periodically
    scheduler = AsyncIOScheduler()
    scheduler.add_job(sync_subscriptions, "interval", seconds=1)  # Run every hour
    scheduler.start()
