from nltk.corpus import wordnet as wn
from typing import List, Any
from models.sense import Sense
from .base import DictionaryProvider

wn: Any  # ← 告诉 pyright: 不要检查 wn 的类型

class WordNetProvider(DictionaryProvider):

    def lookup(self, word: str) -> List[Sense]:
        senses: List[Sense] = []

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
