# Exercise 01 — Logging & config (plan mode)

Part of the Claude Code exercises for the ILIAD intensive. The brief is in the markdown
file next to this one. Exercise 00 is the same steganography experiment as a single script;
here it lives in a structured repo (`experiments/`, `lib/`, a config framework).

```bash
uv sync
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

Needs `OPEN_ROUTER_API_KEY` in `.env` (auto-loaded via direnv). See `CLAUDE.md` for conventions.
