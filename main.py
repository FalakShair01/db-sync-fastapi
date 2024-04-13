from fastapi import FastAPI
from database.db import SessionLocal, engine
from models import subscription_db1, subscription_db2
import periodic_tasks.tasks as tasks
from routers import db1, db2

app = FastAPI()

subscription_db1.Base.metadata.create_all(bind=engine)
subscription_db2.Base.metadata.create_all(bind=engine)

app.include_router(db1.router)
app.include_router(db2.router)

@app.get('/')
async def welcome():
    return "Hello Welcome to database Sync Problem solving task"


@app.on_event("startup")
async def startup_event():
    await tasks.schedule_sync_task()


