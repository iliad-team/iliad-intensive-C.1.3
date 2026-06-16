# Exercise 01 — Logging & Config (plan mode)

## The project: steganographic communication

`experiments/steg_comm` tests whether a model can secretly transmit a sequence of
numbers while answering an ordinary question. Each sample makes two model calls:

1. **Encode** — the model answers a main task and hides the numbers in its answer,
   using an encoding scheme described in the prompt.
2. **Decode** — a second call is given that answer plus the scheme and reads the
   hidden numbers back out.

We score how many of the numbers survive the round-trip.

Run it (needs `OPEN_ROUTER_API_KEY` in `.env`):
```bash
cd experiments/steg_comm
uv run python main.py -c configs/base.yaml
```

Right now the run just `print()`s everything, and all the prompts (system prompt,
encoder/decoder templates, the scheme, the list of main tasks) are hard-coded as
constants in `functions/run_steg.py`.

## Your two tasks

Both suit **plan mode**. Do them as two parallel agents — kick one off and work with
the other while it cooks.

### Task A — log results instead of printing
Make the run write its results to `results/RUN_NAME/` (the scaffold already
substitutes `RUN_NAME`). At minimum a `completions.jsonl` (one row per sample: main
task, values, answer, decoded, correctness) and a `metrics.json` summary. A short
printed summary is fine, but the durable record belongs on disk.

**Done when:** a run produces `results/<run>/completions.jsonl` + `metrics.json` you
can reopen later.

### Task B — move the prompts into config
Move the system prompt, encoder/decoder templates, the scheme, and the main-task list
out of `functions/run_steg.py` and into `configs/base.yaml`, following the template's
rule: **all defaults live in the config, none in Python.**

**Done when:** changing a prompt or the scheme only means editing the config, and
`run_steg.py` has no hard-coded prompt/scheme/task text.

## The technique: plan mode + verify

For each task:
1. Make the agent **plan first** — don't let it one-shot.
2. Read the plan, edit where you disagree, then let it execute.
3. When it's done, **read the diff** and confirm you're happy before moving on.

The point: on multi-file changes with real choices (what to log, which things become
config keys), steering the plan up front beats cleaning up after a one-shot.
