from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from  .infra.database import engine, get_db
from .infra.models import models
from.routes import UserRouter

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(UserRouter.Router)


@app.get('/', response_class=RedirectResponse)
def home():
    return "/redoc"
