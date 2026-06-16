import json


def parse_suspiciousness(content: str) -> int:
    """Pull the integer suspiciousness score out of a monitor's JSON reply."""
    return int(json.loads(content)["suspiciousness"])


async def monitor(client, model, prompt_template, task, output):
    """Ask a model how suspicious `output` looks for `task`. Returns an int score.

    `prompt_template` must contain `{task}` and `{output}` placeholders and ask
    for a JSON reply of the form {"suspiciousness": <int>}.
    """
    resp = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt_template.format(task=task, output=output)}],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return parse_suspiciousness(resp.choices[0].message.content)
