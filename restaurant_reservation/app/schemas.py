from pydantic import BaseModel, EmailStr
from datetime import datetime

class ReservationBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    date_time: datetime
    number_of_people: int

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int

    class Config:
        orm_mode = True
