from nltk.corpus import wordnet as wn

import config
from pipeline import Pipeline
from providers.ai.openai_provider import OpenAIProvider
from providers.ai.qiniu_provider import QiniuProvider
from providers.anki.anki_provider import AnkiProvider
from providers.dictionary.wordnet_provider import WordNetProvider


def init():
    wn.synsets("test")


if __name__ == "__main__":
    import sys

    word = sys.argv[1]

    configuration = config.load_config()
    system_prompt_path = f"prompts/{configuration.ai.model}/system.md"
    user_prompt_path = f"prompts/{configuration.ai.model}/user.md"

    provider = {
        "openai":OpenAIProvider(
            configuration.ai.api_key,
            configuration.ai.model,
            system_prompt_path=system_prompt_path,
            user_prompt_path=user_prompt_path,
        ),
        "qiniu": QiniuProvider(
            configuration.ai.api_key,
            configuration.ai.model,
            configuration.ai.url,
            system_prompt_path=system_prompt_path,
            user_prompt_path=user_prompt_path,
        )
    }.get(configuration.ai.provider,"openai")

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
