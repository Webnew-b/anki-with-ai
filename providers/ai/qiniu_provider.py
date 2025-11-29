# providers/ai/qiniu_provider.py
import json
import requests
from openai import OpenAI

from models.sense import Sense, FinalSense
from providers.ai.base import AIProvider
from utils.prompt_loader import load_prompt


class QiniuProvider(AIProvider):

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str,
        system_prompt_path="prompts/ai/gpt-5/system.md",
        user_prompt_path="prompts/ai/gpt-5/user.md",
    ):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url or "https://qianwen.qiniuapi.com/v1"

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

        self.system_prompt = load_prompt(system_prompt_path)
        self.user_template = load_prompt(user_prompt_path)

    def generate(self, word: str, senses: list[Sense]) -> FinalSense:

        # 转换 WordNet senses → JSON
        senses_json = json.dumps(
            [s.__dict__ for s in senses],
            ensure_ascii=False,
            indent=2,
        )

        # 填充 prompt 模板
        user_prompt = (
            self.user_template
            .replace("{{WORD}}", word)
            .replace("{{SENSES}}", senses_json)
        )

        # 根据你提供的模板，构造 messages
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=False,
            max_tokens=4096         # 按你提供的示例加入
        )

        # 统一按 openai 兼容格式解析
        content = response.choices[0].message.content
        print(f"Get content:{content}")

        result_json = json.loads(content)

        return FinalSense(**result_json)
