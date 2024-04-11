from fastapi import FastAPI
from database.db import SessionLocal, engine
from models import subscription1
import periodic_tasks.tasks as tasks


app = FastAPI()

subscription1.Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    await tasks.schedule_sync_task()


