from app.graph.state import AgentState


def retrieve_evidence(state: AgentState) -> dict:
    return {
        "retrieved_evidence": [
            {
                "repo": "shreyas-evidence",
                "path": "projects/project-001.md",
                "section": "Overview",
                "text": "Placeholder evidence chunk for Shreyas' project work.",
            }
        ]
    }