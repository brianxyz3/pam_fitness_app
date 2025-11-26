import json
from fastapi import APIRouter
from app.models.plan import Plan
from pathlib import Path

router = APIRouter()

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "plans.json"

@router.get("/", response_model=list[Plan])
def get_plans():
    with open(DATA_PATH, "r") as f:
        return json.load(f)
