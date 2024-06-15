from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate):
    return crud.create_reservation(reservation)

@router.get("/", response_model=List[schemas.Reservation])
def read_reservations(skip: int = 0, limit: int = 10):
    return crud.get_reservations(skip=skip, limit=limit)

@router.get("/{reservation_id}", response_model=schemas.Reservation)
def read_reservation(reservation_id: int):
    reservation = crud.get_reservation(reservation_id)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.put("/{reservation_id}", response_model=schemas.Reservation)
def update_reservation(reservation_id: int, reservation: schemas.ReservationCreate):
    updated_reservation = crud.update_reservation(reservation_id, reservation)
    if updated_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation

@router.delete("/{reservation_id}", response_model=schemas.Reservation)
def delete_reservation(reservation_id: int):
    if not crud.delete_reservation(reservation_id):
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {"msg": "Reservation deleted successfully"}
