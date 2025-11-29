from nltk.corpus import wordnet as wn
from typing import List
from models.sense import Sense
from .base import DictionaryProvider


class WordNetProvider(DictionaryProvider):

    def lookup(self, word: str) -> List[Sense]:
        senses = []

        synsets = wn.synsets(word)
        synsets = synsets[:10]  # 限制最多10个义项

        for s in synsets:
            senses.append(
                Sense(
                    synset=s.name(),
                    pos=s.pos(),
                    definition=s.definition(),
                    examples=s.examples(),
                    lemmas=[l.name() for l in s.lemmas()],
                    hypernyms=[h.name() for h in s.hypernyms()],
                    hyponyms=[h.name() for h in s.hyponyms()],
                )
            )
        return senses
