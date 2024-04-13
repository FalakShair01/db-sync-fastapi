from pydantic import BaseModel


class Subscription(BaseModel):
    email: str
    active: bool