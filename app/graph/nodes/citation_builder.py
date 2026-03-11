from app.graph.state import AgentState


def build_citations(state: AgentState) -> dict:
    citations = []

    for fact in state.get("selected_facts", []):
        citations.append(
            {
                "repo": fact.get("repo", ""),
                "path": fact.get("path", ""),
                "section": fact.get("section", ""),
            }
        )

    return {"citations": citations}