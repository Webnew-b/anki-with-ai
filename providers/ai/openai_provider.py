# providers/ai/openai_provider.py
import json
from openai import OpenAI
from models.sense import Sense, FinalSense
from providers.ai.base import AIProvider, serde_json_from_content
from utils.prompt_loader import load_prompt
import config


class OpenAIProvider(AIProvider):

    def __init__(
        self,
        api_key: str,
        model: str,
        system_prompt_path="prompts/ai/gpt-5/system.md",
        user_prompt_path="prompts/ai/gpt-5/user.md",
    ):
        self.client = OpenAI(api_key=api_key)
        self.model = model

        self.system_prompt = load_prompt(system_prompt_path)
        self.user_template = load_prompt(user_prompt_path)

    def generate(self, word: str, senses: list[Sense]) -> FinalSense:

        senses_json = json.dumps(
            [s.__dict__ for s in senses],
            ensure_ascii=False,
            indent=2
        )

        user_prompt = (
            self.user_template
            .replace("{{WORD}}", word)
            .replace("{{SENSES}}", senses_json)
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content
        print(f"Get content: {content}")

        return serde_json_from_content(content)
