from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os 

load_dotenv()
pipe = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipe
    model_name = os.getenv("MODEL_NAME")
    if not model_name:
        raise ValueError("MODEL_NAME environment variable not set.")
    pipe = pipeline("sentiment-analysis", model=model_name)
    print("Model loaded.")
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request,name='index.html')


@app.post("/", response_class=HTMLResponse)
async def analyze_sentiment(request: Request, text: str = Form(...)):
    try:
        result = pipe(text)[0]
        return templates.TemplateResponse("index.html", {
            "request": request,
            "text": text,
            "label": result['label'],
            "score": f"{result['score']:.4f}",
            "result": True
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })

@app.post("/api/analyze")
async def analyze_api(input: TextInput):
    try:
        result = pipe(input.text)[0]
        return {
            "text": input.text,
            "sentiment": result['label'],
            "confidence": result['score']
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

