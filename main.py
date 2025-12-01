from typing import Any

from nltk.corpus import wordnet as wn

wn:Any

import config
from pipeline import Pipeline
from providers.ai.base import AIProvider
from providers.ai.openai_provider import OpenAIProvider
from providers.ai.qiniu_provider import QiniuProvider
from providers.anki.anki_provider import AnkiProvider
from providers.dictionary.wordnet_provider import WordNetProvider


def init() -> None:
    wn.synsets("test")


def init_provider(provider_name: str, config: config.AppConfig) -> AIProvider:
    system_prompt_path = f"prompts/{configuration.ai.model}/system.md"
    user_prompt_path = f"prompts/{configuration.ai.model}/user.md"
    if provider_name == "openai":
        return OpenAIProvider(
            config.ai.api_key,
            config.ai.model,
            system_prompt_path=system_prompt_path,
            user_prompt_path=user_prompt_path,
        )
    elif provider_name == "qiniu":
        return QiniuProvider(
            config.ai.api_key,
            config.ai.model,
            config.ai.url,
            system_prompt_path=system_prompt_path,
            user_prompt_path=user_prompt_path,
        )
    else:
        raise ValueError(f"Unknown provider: {provider_name}")


if __name__ == "__main__":
    import sys

    word = sys.argv[1]

    configuration: config.AppConfig = config.load_config()

    provider: AIProvider = init_provider("qiniu", configuration)

    pipe = Pipeline(
        dict_provider=WordNetProvider(),
        ai_provider=provider,
        anki_provider=AnkiProvider(
            url=configuration.anki.url,
            deck=configuration.anki.deck,
            model=configuration.anki.model
        ),
    )

    result = pipe.run(word)
    print(result)
