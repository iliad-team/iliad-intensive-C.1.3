# Exercise 00 — One script (ask, edit, run, read the diff)

## The project: steganographic communication

`steg.py` tests whether a model can secretly transmit a sequence of numbers while
answering an ordinary question. Each sample makes two model calls:

1. **Encode** — the model answers a main task and hides the numbers in its answer,
   using an encoding scheme described in the prompt.
2. **Decode** — a second call is given that answer plus the scheme and reads the
   hidden numbers back out.

We score how many of the numbers survive the round-trip.

That's the whole repo: one script, everything hard-coded inline. No folders, no
framework. Run it (needs `OPEN_ROUTER_API_KEY` in `.env`):

```bash
uv run python steg.py
```

## Step 1 — Get oriented

Start `claude` in this folder and ask it what `steg.py` does.

Then **write a three-line summary in your own words**, and check every claim against
the file. If Claude says something you can't find in the code, ask it to point to the
line. The rule for this whole course: don't accept an explanation you can't verify.

## Step 2 — Run it

Run the script and read the output. What did the model write? Did the decoder get the
numbers back? What's the accuracy at the bottom?

## Task A — log results instead of printing

Right now the run just `print()`s everything and is gone when the terminal scrolls.
Have Claude make it write results to disk: a folder per run (e.g.
`results/<timestamp>/`) containing a `completions.jsonl` (one row per sample: main
task, values, answer, decoded, correctness) and a `metrics.json` summary. A short
printed summary is fine, but the durable record belongs on disk.

**Done when:** a run produces a results folder you can reopen later.

## Task B — move the settings into a YAML config

Everything that could change between runs — the model, the number of samples, the
prompts, the scheme, the list of main tasks — is scattered through `steg.py`.
Move it all into `configs/base.yaml` and make the script take the config path from
the terminal:

```bash
uv run python steg.py --config configs/base.yaml
```

Claude will need to add a YAML library; let it do so with `uv add`, not by editing
`pyproject.toml`.

**Done when:** changing a prompt or setting only means editing the YAML, and
`steg.py` contains no hard-coded prompt, scheme, or settings. Bonus: add a
`configs/debug.yaml` with one or two samples for quick runs.

## The technique: ask → edit → run → read the diff

For every task:

1. Describe what you want in plain words. Say what "done" looks like.
2. Before accepting a change, **read the diff** (`git diff`, or the diff Claude shows
   you). Make sure you understand each change. Ask about anything you don't.
3. Run it. If it's wrong, tell Claude *what happened* (paste the output) rather than
   fixing it by hand.
4. Commit when it works, so the next task starts from a clean diff.

## What's next

In exercise 01 you'll do these same two tasks again — but in a properly structured
repo (an `experiments/` folder, a shared `lib/`, a config framework). Notice what the
structure buys you, and what it costs.
