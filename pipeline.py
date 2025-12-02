from typing import Optional, Protocol

from providers.ai.base import AIProvider
from providers.anki.anki_provider import AnkiProvider
from providers.dictionary.base import DictionaryProvider
from validators import validate_word

class ProgressReporter(Protocol):
    def __call__(self, status: str, percent: int) -> None:
        ...

class Pipeline:

    def __init__(
            self,
            dict_provider: DictionaryProvider,
            ai_provider: AIProvider,
            anki_provider: AnkiProvider
    ):
        self.dict = dict_provider
        self.ai = ai_provider
        self.anki = anki_provider

    def run(self, word: str,progress: Optional[ProgressReporter] = None):
        def report(status: str, pct: int) -> None:
            if progress is not None:
                progress(status, pct)

        print(f"Input word :{word}")
        print(f"[{word}]Validating the input word.")
        report("validating", 5)
        validate_word(word)

        print(f"[{word}]Lookup the word in the dictionary.")
        report(f"[{word}]querying dictionary", 20)
        senses = self.dict.lookup(word)
        if not senses:
            raise ValueError(f"Word '{word}' not found in dictionary.")

        print(f"[{word}]Generate the word other information by ai.")
        report("AI generating", 60)
        final = self.ai.generate(word, senses)

        print(f"[{word}]Add word to anki")
        report("importing to Anki", 85)
        self.anki.add(final)
        print(f"[{word}]Add word to anki success.")

        report("done", 100)
        return final
