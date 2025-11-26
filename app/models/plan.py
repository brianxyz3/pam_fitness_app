from pydantic import BaseModel

class Plan(BaseModel):
    id: int
    name: str
    difficulty: str
    duration_weeks: int
