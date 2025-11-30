from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Sense:
    synset: str
    pos: str
    definition: str
    examples: List[str]
    lemmas: List[str]
    hypernyms: List[str]
    hyponyms: List[str]

@dataclass
class OtherPos:
    pos: str
    definition: str
    examples_dict: List[str]
    examples_ai: List[str]

@dataclass
class FinalSense:
    word: str
    synset: str
    pos: str
    definition: str
    definition_simple: str
    hypernyms: List[str]
    hyponyms: List[str]
    synonyms: List[str]
    examples_dict: List[str]
    examples_ai: List[str]
    other_pos: List[OtherPos]
    chinese: str
