from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get('/', response_class=RedirectResponse)
def home():
    return "/redoc"