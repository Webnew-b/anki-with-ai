# utils/prompt_loader.py
from pathlib import Path

def load_prompt(path: str) -> str:
    full_path = Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return full_path.read_text(encoding="utf-8")
