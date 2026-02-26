from pathlib import Path
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.rag import ask_rag

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[3]
templates = Jinja2Templates(directory=str(BASE_DIR / "frontend/templates"))

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    answer = ask_rag(message)

    return templates.TemplateResponse(
        "chat.html",
        {"request": request, "message": message, "answer": answer}
    )
