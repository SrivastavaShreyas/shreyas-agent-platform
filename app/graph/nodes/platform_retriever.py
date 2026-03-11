from app.graph.state import AgentState


def retrieve_platform(state: AgentState) -> dict:
    return {
        "retrieved_platform": [
            {
                "repo": "shreyas-platform-docs",
                "path": "architecture/overview.md",
                "section": "Architecture",
                "text": "Placeholder platform chunk explaining Kubernetes, Argo CD, Qdrant, and Open WebUI.",
            }
        ]
    }