from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.db import Base

# Assuming this is DB1 Subscription Table
class Subscription1(Base):
    __tablename__ = "subscriptions1"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)    
    active = Column(Boolean, index=True)

