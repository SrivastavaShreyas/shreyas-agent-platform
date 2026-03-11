from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)
    jd_text: Optional[str] = None
    company_context: Optional[str] = None


class ChatResponse(BaseModel):
    task_type: str
    answer: str
    citations: List[Dict[str, Any]] = Field(default_factory=list)