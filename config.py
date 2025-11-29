# config/config.py
from dataclasses import dataclass
from pathlib import Path
from dotenv import dotenv_values


@dataclass
class AIConfig:
    api_key: str
    model: str
    provider: str
    url:str


@dataclass
class AnkiConfig:
    url: str
    deck: str
    model: str


@dataclass
class AppConfig:
    ai: AIConfig
    anki: AnkiConfig


def load_config(env_path: str = ".env") -> AppConfig:
    """显式加载配置，不在 import 时加载"""
    if not Path(env_path).exists():
        raise FileNotFoundError(f"{env_path} not found")

    env = dotenv_values(env_path)

    ai = AIConfig(
        api_key=env.get("AI_API_KEY", ""),
        model=env.get("AI_MODEL", "gpt-5"),
        provider=env.get("AI_PROVIDER", "openai"),
        url=env.get("AI_API_URL","")
    )

    anki = AnkiConfig(
        url=env.get("ANKI_CONNECT_URL", "http://localhost:8765"),
        deck=env.get("ANKI_DECK", "English"),
        model=env.get("ANKI_MODEL", "VocabModel"),
    )

    return AppConfig(ai=ai, anki=anki)
