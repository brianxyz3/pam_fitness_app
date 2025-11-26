import json
from fastapi import APIRouter
from app.models.employee import Employee
from pathlib import Path

router = APIRouter()

employees_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "employees.json"
print(employees_PATH)

@router.get("/", response_model=list[Employee])
def get_employees():
    with open(employees_PATH, "r") as f:
        return json.load(f)
    
