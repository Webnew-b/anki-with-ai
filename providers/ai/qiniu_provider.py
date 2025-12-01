from __future__ import annotations

import json
from typing import List

from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from models.sense import Sense, FinalSense
from providers.ai.base import AIProvider, serde_json_from_content
from utils.prompt_loader import load_prompt


class QiniuProvider(AIProvider):

    def __init__(
            self,
            api_key: str,
            model: str,
            base_url: str,
            system_prompt_path: str = "prompts/ai/gpt-5/system.md",
            user_prompt_path: str = "prompts/ai/gpt-5/user.md",
    ) -> None:
        self.api_key = api_key
        self.model = model

        # 七牛直接兼容 OpenAI，base_url 必须指向七牛
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        self.system_prompt = load_prompt(system_prompt_path)
        self.user_template = load_prompt(user_prompt_path)

    def generate(self, word: str, senses: List[Sense]) -> FinalSense:
        senses_json = json.dumps(
            [s.__dict__ for s in senses],
            ensure_ascii=False,
        )

        user_prompt = (
            self.user_template
            .replace("{{WORD}}", word)
            .replace("{{SENSES}}", senses_json)
        )

        messages: List[
            ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam
            ] = [
            ChatCompletionSystemMessageParam(
                role="system",
                content=self.system_prompt,
            ),
            ChatCompletionUserMessageParam(
                role="user",
                content=user_prompt,
            ),
        ]

        response: ChatCompletion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=False,
            max_tokens=4096,
        )

        message: ChatCompletionMessage = response.choices[0].message
        content = message.content

        if content is None:
            raise ValueError("Qiniu (OpenAI compatible) returned empty content")

        print(f"Get result: {content}")

        res = serde_json_from_content(content)

        return res
