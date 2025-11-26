from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    speciality: str
    certification: Optional[str] = None
    imageSrc: str
    experience_years: int
    bio: str

