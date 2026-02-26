from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import chat

app = FastAPI(title="ICICI RAG Chatbot")

# templates
templates = Jinja2Templates(directory="../../frontend/templates")

# routers
app.include_router(chat.router)
    