# Shreyas Agent Platform

This repository contains the application layer for an AI-driven recruiter interaction platform about Shreyas Srivastava.

## Main responsibilities
•⁠  ⁠expose chat API
•⁠  ⁠orchestrate agent workflow
•⁠  ⁠retrieve grounded evidence from indexed repositories
•⁠  ⁠analyze role descriptions
•⁠  ⁠answer questions about Shreyas and about the platform itself

## Main modules
•⁠  ⁠⁠ app/api ⁠ - FastAPI endpoints
•⁠  ⁠⁠ app/graph ⁠ - LangGraph orchestration
•⁠  ⁠⁠ app/tools ⁠ - shared utilities
•⁠  ⁠⁠ app/ingest ⁠ - indexing pipelines
•⁠  ⁠⁠ app/prompts ⁠ - LLM prompt files

## First milestone
Run the API locally and return graph-driven responses from stubbed nodes.

## Local run
```bash
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000

----

## `app/api/schemas.py`

```python
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