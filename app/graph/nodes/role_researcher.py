from app.graph.state import AgentState
from app.tools.jd_parser import parse_jd_text


def analyze_role(state: AgentState) -> dict:
    jd_text = state.get("jd_text")
    if not jd_text:
        return {"retrieved_research": []}

    parsed = parse_jd_text(jd_text)
    return {"retrieved_research": [parsed]}