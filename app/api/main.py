from fastapi import FastAPI, HTTPException
from app.api.schemas import ChatRequest, ChatResponse
from app.graph.build_graph import build_agent_graph
from app.tools.config import settings

app = FastAPI(title=settings.app_name)
graph = build_agent_graph()


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    question = req.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="question cannot be empty")

    result = graph.invoke(
        {
            "user_question": question,
            "jd_text": req.jd_text,
            "company_context": req.company_context,
            "errors": [],
        }
    )

    return ChatResponse(
        task_type=result.get("task_type", "unknown"),
        answer=result.get("answer", "No answer generated."),
        citations=result.get("citations", []),
    )