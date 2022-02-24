
from ..schemas.schemas import UserCreate
from ..providers.hashCrypt import password_hash_generate, verify_password
from ..infra.models import models
from sqlalchemy.orm import Session

from fastapi import HTTPException, status
from email_validator import validate_email, EmailNotValidError

class UserService:
    
    def __init__(self, db: Session) -> None:
        self.db = db
        
    async def create(self, user: UserCreate):


        try:
            validate_email(user.email)
        except EmailNotValidError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "email is not valid."}
            )

        is_existis = await self.find_by_email(user.email)
        
        if is_existis:
            raise HTTPException(
                status_code=404,
                detail={"message": "email already existis."}
            )
        
        password = password_hash_generate(user.password)
        db_user = models.User(
            username=user.username,
            email=user.email,
            hashed_password=password
            )
        
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        
        return db_user

    async def find_by_id(self, id: int):
        return self.db.query(models.User).filter(models.User.id == id).first()

    async def find_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()
