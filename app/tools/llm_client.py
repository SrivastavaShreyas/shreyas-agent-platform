import httpx
from app.tools.config import settings


def chat(messages: list[dict], temperature: float = 0.2) -> str:
    payload = {
        "model": settings.llm_model,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature},
    }

    response = httpx.post(
        f"{settings.llm_base_url}/api/chat",
        json=payload,
        timeout=60.0,
    )
    response.raise_for_status()
    data = response.json()

    return data.get("message", {}).get("content", "")