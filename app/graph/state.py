from typing import TypedDict, Optional, List, Dict, Any


class AgentState(TypedDict, total=False):
    user_question: str
    jd_text: Optional[str]
    company_context: Optional[str]

    task_type: str

    retrieved_evidence: List[Dict[str, Any]]
    retrieved_platform: List[Dict[str, Any]]
    retrieved_research: List[Dict[str, Any]]

    selected_facts: List[Dict[str, Any]]
    answer: str
    citations: List[Dict[str, Any]]
    errors: List[str]