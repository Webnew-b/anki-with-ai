import requests
from models.sense import FinalSense


class AnkiProvider:

    def __init__(self, deck="English", model="VocabModel",url="http://localhost:8765"):
        self.deck = deck
        self.model = model
        self.url = url

    def add(self, sense: FinalSense):

        note = {
            "deckName": self.deck,
            "modelName": self.model,
            "fields": {
                "Word": sense.word,
                "Definition": sense.definition,
                "Definition Simple": sense.definition_simple,
                "Hypernyms": ", ".join(sense.hypernyms),
                "Hyponyms": ", ".join(sense.hyponyms),
                "Synonyms": ", ".join(sense.synonyms),
                "WordNet Examples": "\n".join(sense.examples_wordnet),
                "AI Examples": "\n".join(sense.examples_ai),
                "Chinese": sense.chinese,
                "POS": sense.pos
            },
            "options": {"allowDuplicate": False},
            "tags": ["auto"],
        }

        payload = {
            "action": "addNote",
            "version": 6,
            "params": {"note": note},
        }

        requests.post(self.url, json=payload)
