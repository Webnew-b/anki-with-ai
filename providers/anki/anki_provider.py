import requests
from models.sense import FinalSense
from utils.template_loader import render_card_html


class AnkiProvider:

    def __init__(self,
                 deck: str = "English",
                 model: str = "VocabModel",
                 url: str = "http://localhost:8765"
    ):
        self.deck = deck
        self.model = model
        self.url = url

    def add(self, sense: FinalSense):
        # 调用你之前的 Jinja2 渲染函数
        front_card = render_card_html(sense, "front_card_template.html")
        back_content = render_card_html(sense,"back_card_template.html")

        # 构造一个新的 Anki Note
        note = {
            "deckName": self.deck,
            "modelName": self.model,
            "fields": {
                "Word": sense.word,  # 方便搜索
                "Front": front_card,  # 主体内容：主义项 + other_pos + CSS
                "Back":back_content
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

