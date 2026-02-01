from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[str]
    title: str
    description: Optional[str]
    completed: bool = False