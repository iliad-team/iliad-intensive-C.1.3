# ILIAD Intensive C.1.3 — Claude Code exercises

Hands-on exercises for learning to work with Claude Code on a small ML research
codebase. The running project is a steganography study: can a model secretly
transmit numbers inside an ordinary answer, and can a monitor catch it?

Each exercise is a branch:

| Branch | Topic |
|---|---|
| `claude_code_exercise/00` | One script — ask, edit, run, read the diff |
| `claude_code_exercise/01` | Logging & config — plan mode |
| `claude_code_exercise/02` | Monitor & schemes — subagents |
| `claude_code_exercise/03` | Best scheme & self-invented schemes — worktrees + goal |

Check one out and read its `EXERCISE.md`:

```bash
git checkout claude_code_exercise/01
```

Setup: [uv](https://docs.astral.sh/uv/) manages deps, and runs need an
`OPEN_ROUTER_API_KEY` in `.env` (auto-loaded via direnv).

```bash
uv sync
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

See `CLAUDE.md` for the repo conventions.
