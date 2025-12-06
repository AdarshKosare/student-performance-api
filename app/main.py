from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import numpy as np

from .schemas import PredictionRequest
from .model_loader import load_models

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load all three models
linear, lasso, ridge = load_models()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "linear": None,
        "lasso": None,
        "ridge": None
    })

@app.post("/", response_class=HTMLResponse)
def home_predict(
    request: Request,
    study_hours: float = Form(...),
    previous_score: float = Form(...),
    sleep_hours: float = Form(...),
    practiced_sample_paper_count: int = Form(...),
    extracurricular_activities: bool = Form(...)
):

    X = np.array([[ 
        study_hours,
        previous_score,
        sleep_hours,
        practiced_sample_paper_count,
        extracurricular_activities
    ]])

    pred_linear = linear.predict(X)[0]
    pred_lasso = lasso.predict(X)[0]
    pred_ridge = ridge.predict(X)[0]

    return templates.TemplateResponse("home.html", {
        "request": request,
        "linear": round(float(pred_linear), 2),
        "lasso": round(float(pred_lasso), 2),
        "ridge": round(float(pred_ridge), 2)
    })
