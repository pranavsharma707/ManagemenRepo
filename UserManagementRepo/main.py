from fastapi import FastAPI
from settings import engine
import models
from app import views

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


app = FastAPI(title="UserManagement api",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(GZipMiddleware)
models.Base.metadata.create_all(bind=engine)
app.include_router(views.router)

