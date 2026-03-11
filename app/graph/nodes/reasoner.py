from app.graph.state import AgentState


def reason_over_context(state: AgentState) -> dict:
    selected_facts = []

    for item in state.get("retrieved_evidence", []):
        selected_facts.append(item)

    for item in state.get("retrieved_platform", []):
        selected_facts.append(item)

    for item in state.get("retrieved_research", []):
        selected_facts.append(item)

    return {"selected_facts": selected_facts}