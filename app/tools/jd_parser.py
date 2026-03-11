def parse_jd_text(jd_text: str) -> dict:
    lowered = jd_text.lower()

    keywords = []
    for candidate in [
        "kubernetes",
        "aws",
        "azure",
        "grafana",
        "prometheus",
        "terraform",
        "argo cd",
        "python",
        "sre",
        "devops",
        "platform",
        "observability",
    ]:
        if candidate in lowered:
            keywords.append(candidate)

    return {
        "repo": "runtime",
        "path": "jd_input",
        "section": "parsed_jd",
        "text": f"Parsed JD keywords: {', '.join(keywords) if keywords else 'none detected'}",
        "keywords": keywords,
    }