from fastapi import FastAPI
from app.routers import reservation
from app.database import init_db

app = FastAPI()

# Inicializar la base de datos
init_db()

# Incluir las rutas
app.include_router(reservation.router)
