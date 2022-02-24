from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from  .infra.database import engine, get_db
from .infra.models import models
from sqlalchemy.orm import Session
from .services.UserService import UserService
from .schemas import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = UserService(db)
    new_user = await db_user.create(user)
    return new_user

    