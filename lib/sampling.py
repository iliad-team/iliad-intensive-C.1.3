import os

from openai import AsyncOpenAI


def build_messages(prompt: str, system: str | None = None) -> list[dict]:
    """Assemble a chat message list, with an optional system turn first."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    return messages


def make_client(api_key: str | None = None, base_url: str = "https://openrouter.ai/api/v1") -> AsyncOpenAI:
    return AsyncOpenAI(api_key=api_key or os.environ["OPEN_ROUTER_API_KEY"], base_url=base_url)


async def sample(client, model, prompt, system=None, *, max_tokens, temperature):
    """One chat completion. Returns the message content (empty string if none)."""
    resp = await client.chat.completions.create(
        model=model,
        messages=build_messages(prompt, system),
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""
