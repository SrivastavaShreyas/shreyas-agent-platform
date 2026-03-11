from app.graph.state import AgentState


def write_answer(state: AgentState) -> dict:
    task_type = state.get("task_type", "about_me")
    facts = state.get("selected_facts", [])

    fact_lines = []
    for fact in facts:
        text = fact.get("text", "")
        if text:
            fact_lines.append(f"- {text}")

    if not fact_lines:
        fact_lines.append("- No supporting facts were retrieved.")

    answer = (
        f"Task type: {task_type}\n\n"
        "This is the current dynamically assembled response using selected facts:\n"
        + "\n".join(fact_lines)
    )

    return {"answer": answer}