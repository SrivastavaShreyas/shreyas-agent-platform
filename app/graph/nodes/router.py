from app.graph.state import AgentState


def route_question(state: AgentState) -> dict:
    question = state["user_question"].lower()

    platform_terms = [
        "platform",
        "architecture",
        "argo cd",
        "gitops",
        "kubernetes",
        "how was this built",
        "how did shreyas build this",
        "deployment",
    ]

    role_terms = [
        "job description",
        "jd",
        "fit",
        "align",
        "alignment",
        "match this role",
        "suitable for",
        "role",
    ]

    if any(term in question for term in platform_terms):
        task_type = "platform_explain"
    elif state.get("jd_text") or any(term in question for term in role_terms):
        task_type = "role_alignment"
    else:
        task_type = "about_me"

    return {"task_type": task_type}