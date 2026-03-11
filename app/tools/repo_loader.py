from pathlib import Path


def load_text_documents(repo_path: str) -> list[dict]:
    docs = []
    if not repo_path:
        return docs

    base = Path(repo_path)
    if not base.exists():
        return docs

    for path in base.rglob("*"):
        if path.is_file() and path.suffix in [".md", ".txt", ".yaml", ".yml"]:
            docs.append(
                {
                    "path": str(path.relative_to(base)),
                    "text": path.read_text(encoding="utf-8", errors="ignore"),
                }
            )
    return docs