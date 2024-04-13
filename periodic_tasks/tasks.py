from fastapi import Depends
from sqlalchemy.orm import Session
from models.subscription_db1 import Subscription1
from models.subscription_db2 import Subscription2
from database.db import get_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def sync_subscriptions(db_session: Session):
    try:
        # Filter inactive subscriptions from db2
        inactive_subscriptions = db_session.query(Subscription2).filter(Subscription2.active == False).all()
        
        # Check status of inactive subscriptions in db1
        for subscription in list(inactive_subscriptions):
            email = subscription.email
            status_db1 = get_subscription_status_from_db1(db_session, email)
            if status_db1 == True:
                # Update entry in db2
                subscription.active = True  
                db_session.commit()
    except Exception as e:
        print(str(e))

def get_subscription_status_from_db1(db_session: Session, email: str) -> str:
    subscription = db_session.query(Subscription1).filter(Subscription1.email == email).first()
    return subscription.active if subscription else False  


async def schedule_sync_task(db_session: Session = Depends(get_db)):
    # Schedule sync task to run periodically
    scheduler = AsyncIOScheduler()
    scheduler.add_job(sync_subscriptions, "interval", seconds=10, args=[db_session])  # Pass db_session as an argument
    scheduler.start()
