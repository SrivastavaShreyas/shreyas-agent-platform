from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.graph.nodes.router import route_question
from app.graph.nodes.evidence_retriever import retrieve_evidence
from app.graph.nodes.platform_retriever import retrieve_platform
from app.graph.nodes.role_researcher import analyze_role
from app.graph.nodes.reasoner import reason_over_context
from app.graph.nodes.answer_writer import write_answer
from app.graph.nodes.citation_builder import build_citations


def _route_after_router(state: AgentState) -> str:
    task_type = state.get("task_type", "about_me")

    if task_type == "about_me":
        return "evidence_retriever"
    if task_type == "platform_explain":
        return "platform_retriever"
    if task_type == "role_alignment":
        return "role_researcher"
    return "evidence_retriever"


def build_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", route_question)
    graph.add_node("evidence_retriever", retrieve_evidence)
    graph.add_node("platform_retriever", retrieve_platform)
    graph.add_node("role_researcher", analyze_role)
    graph.add_node("reasoner", reason_over_context)
    graph.add_node("answer_writer", write_answer)
    graph.add_node("citation_builder", build_citations)

    graph.set_entry_point("router")
    graph.add_conditional_edges("router", _route_after_router)

    graph.add_edge("evidence_retriever", "reasoner")
    graph.add_edge("platform_retriever", "reasoner")
    graph.add_edge("role_researcher", "evidence_retriever")
    graph.add_edge("reasoner", "answer_writer")
    graph.add_edge("answer_writer", "citation_builder")
    graph.add_edge("citation_builder", END)

    return graph.compile()