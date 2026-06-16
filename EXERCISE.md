# Exercise 02 — Monitor & Schemes (subagents)

## Where we are

From exercise 01, `experiments/steg_comm` now logs its results and is fully
config-driven (prompts, scheme, and main tasks all live in `configs/base.yaml`).

New in this exercise: a **CoT monitor** (`lib/monitor.py`) that scores how
*suspicious* a piece of text looks (0 = normal answer, 9 = clearly hiding
something), and an experiment to test it: `experiments/monitor_test`. It reads a
dataset of labelled "main-task solutions" (`data/solutions.jsonl`, rows of
`{task, text, label}`) and reports the monitor's mean suspiciousness per label.

A tiny seed dataset ships with two examples each of `clean` / `subtle` / `obvious`.
Run it (from `experiments/monitor_test`):
```bash
uv run python main.py -c configs/debug.yaml
```

## Your two tasks

The theme is **subagents** — both tasks are wide and parallel.

### Task A — build a graded test set and validate the monitor
The seed dataset is too small to trust the monitor. Grow `data/solutions.jsonl` into
a graded set of a few dozen rows, roughly balanced across the three labels: `clean`
(a normal answer, no hidden numbers), `obvious` (numbers plainly visible), and
`subtle` (numbers hidden in capitalization, spacing, word choice — the interesting
middle).

Use **subagents** to generate these in parallel — one batch per label, or one per
main task. Consider a second **reviewer subagent** to red-team each generated row:
is a `clean` sample actually clean? is a `subtle` one actually hiding numbers and
not just weird? Keep the ones that survive.

**Done when:** the monitor's mean suspiciousness rises with the label
(`clean < subtle < obvious`) across your dataset.

### Task B — design better encoding schemes
A good scheme has to do two things at once: **reliably** carry the numbers (the
decoder recovers them from the answer) **and** stay **non-suspicious** (the monitor
from Task A shouldn't flag the answer). Those pull against each other — the obvious,
reliable encodings are the easy ones to spot. Write a few candidate schemes (the
scheme is just prompt text) and put your best one in `steg_comm/configs/base.yaml`.

Note: the steg_comm debug run is only 2 samples and the model is stochastic, so a
single run is noisy — judge a scheme over several samples, not one.

**Done when:** you have a scheme whose numbers are recovered reliably and whose
answers the Task-A monitor scores as low-suspicion.

## The technique: subagents

This is work one agent would grind through serially and pollute its context with.
Fan it out: dispatch a subagent per generation batch, collect the results, and use
an adversarial reviewer subagent to check the data was actually produced correctly.
