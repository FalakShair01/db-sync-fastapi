from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.db import Base

# Assuming this is DB2 Subscription Table
class Subscription2(Base):
    __tablename__ = "subscriptions2"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)    
    status = Column(String, index=True)
