# ML Research Template

A template where every experiment is a self-contained study — training, eval,
data generation, analysis — that you can read, run, and reproduce on its own.

The idea:

- **Experiments are isolated.** Each lives in its own folder under
  `experiments/`, with its own entry point, functions, configs, and results.
- **Config drives everything.** An experiment is a function plus a YAML config.
  Defaults live in the config, never in Python — a missing key crashes rather
  than guessing.
- **One pattern scales.** The same config format runs a single study, a batch of
  variants from a shared base, or a wandb sweep. Its shape decides which.
- **Shared code stays small.** Reusable bits live in an installable `lib/`
  package; everything experiment-specific stays in the experiment.

Run one from its folder ([uv](https://docs.astral.sh/uv/) manages deps):

```bash
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

See `CLAUDE.md` for the full conventions.
