from abc import ABC, abstractmethod
from typing import List
from models.sense import Sense


class DictionaryProvider(ABC):

    @abstractmethod
    def lookup(self, word: str) -> List[Sense]:
        pass
