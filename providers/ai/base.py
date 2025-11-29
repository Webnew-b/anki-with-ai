from abc import ABC, abstractmethod
from typing import List, Dict
from models.sense import FinalSense, Sense


class AIProvider(ABC):

    @abstractmethod
    def generate(self, word: str, senses: List[Sense]) -> FinalSense:
        pass
