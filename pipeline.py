from providers.ai.base import AIProvider
from providers.anki.anki_provider import AnkiProvider
from providers.dictionary.base import DictionaryProvider
from validators import validate_word


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

    def run(self, word: str):
        print(f"Input word :{word}")
        print("Validating the input word.")
        validate_word(word)

        print("Lookup the word in the dictionary.")
        senses = self.dict.lookup(word)
        if not senses:
            raise ValueError(f"Word '{word}' not found in dictionary.")

        print("Generate the word other information by ai.")
        final = self.ai.generate(word, senses)
        print("Add word to anki")
        self.anki.add(final)
        print("Add word to anki success.")

        return final
