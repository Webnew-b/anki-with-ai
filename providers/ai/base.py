import json
from abc import ABC, abstractmethod
from typing import List
from models.sense import FinalSense, Sense, OtherPos


class AIProvider(ABC):

    @abstractmethod
    def generate(self, word: str, senses: List[Sense]) -> FinalSense:
        pass


def serde_json_from_content(content: str) -> FinalSense:
    result_json = json.loads(content)
    other_pos_list = [
        OtherPos(
            pos=item.get("pos", ""),
            definition=item.get("definition", ""),
            examples_dict=item.get("examples_dict", []),
            examples_ai=item.get("examples_ai", []),
        )
        for item in result_json.get("other_pos", [])
    ]

    return FinalSense(
        word=result_json.get("word", ""),
        synset=result_json.get("synset", ""),
        pos=result_json.get("pos", ""),
        definition=result_json.get("definition", ""),
        definition_simple=result_json.get("definition_simple", ""),
        hypernyms=result_json.get("hypernyms", []),
        hyponyms=result_json.get("hyponyms", []),
        synonyms=result_json.get("synonyms", []),
        examples_dict=result_json.get("examples_dict", []),
        examples_ai=result_json.get("examples_ai", []),
        other_pos=other_pos_list,
        chinese=result_json.get("chinese", ""),
    )
