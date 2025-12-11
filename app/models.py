from pydantic import BaseModel
from typing import Dict, Any


class CreateGraphRequest(BaseModel):
    workflow: str


class RunGraphRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]
