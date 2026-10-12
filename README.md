# ILIAD Intensive C.1.3 — Claude Code exercises

Hands-on exercises for learning to work with Claude Code on a small ML research
codebase. The running project is a steganography study: can a model secretly
transmit numbers inside an ordinary answer, and can a monitor catch it?

## Install Claude Code

Two options: the **VS Code extension** (any OS), or the **terminal CLI** (macOS / Linux;
not recommended on Windows).

**If you already have a Claude account with Claude Code, use that:** skip Step 1 and just
log in when Claude Code asks.

**Step 1 (only without your own account): save the course API key.** The key is shared:
use it only for the course project work and never post it anywhere public. This writes
`~/.claude/settings.json`, which both the extension and the CLI read. You're done when
Claude answers a question without asking you to log in (`/status` shows an "API key" row).

macOS / Linux:

```bash
mkdir -p ~/.claude && echo '{"env":{"ANTHROPIC_API_KEY":"<COURSE_API_KEY>"}}' > ~/.claude/settings.json
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude" | Out-Null; Set-Content "$HOME\.claude\settings.json" '{"env":{"ANTHROPIC_API_KEY":"<COURSE_API_KEY>"}}'
```

Windows only: also install [Git for Windows](https://git-scm.com/downloads/win). It gives
Claude a Bash shell, and the course assumes Bash.

**Step 2: pick one**

- **VS Code** (1.94+): open Extensions (`Cmd+Shift+X` / `Ctrl+Shift+X`), install "Claude Code"
  by Anthropic, open your project folder and the Claude panel (sidebar icon, or `Cmd+Esc` / `Ctrl+Esc`).
  If it asks you to sign in, quit VS Code completely and reopen it.
  [Docs](https://code.claude.com/docs/en/vs-code#install-the-extension)
- **Terminal, macOS / Linux**: `curl -fsSL https://claude.ai/install.sh | bash`, open a new
  terminal, `cd` to your project, run `claude`. Say yes when it asks whether to use the API key.
  [Docs](https://code.claude.com/docs/en/setup#install-claude-code)
- **Terminal, Windows**: in PowerShell, `irm https://claude.ai/install.ps1 | iex`, open a new
  PowerShell or Git Bash window, `cd` to your project, run `claude`. Say yes to the API key.
  [Docs](https://code.claude.com/docs/en/setup#set-up-on-windows)

### Optional: herdr (macOS / Linux)

[herdr](https://herdr.dev/) is a terminal workspace manager built for running several
Claude agents at once (one workspace per project, one tab per branch), and it shows which
agent needs you. Install it with:

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

then run `herdr`. To look at files next to Claude, install [neovim](https://neovim.io/)
(`brew install neovim` on macOS; on Linux use the [release binaries](https://github.com/neovim/neovim/blob/master/INSTALL.md),
apt's version is too old) with [LazyVim](https://www.lazyvim.org/installation).
Plain neovim already takes mouse clicks and scrolling; LazyVim adds a file tree and tabs you
can click.

For a ready-made setup (herdr, keybindings, neovim, Claude settings), see
the minimal version of my dotfiles: [wusche1/dotfiles @ minimal](https://github.com/wusche1/dotfiles/tree/minimal).

### Cheat sheets

- Claude Code: https://www.alignment-hive.com/cheatsheet
- herdr: https://cskwork.github.io/herdr-cheatsheet/

## Exercises

Each exercise is a branch and adds one technique: the basic ask → edit → run → read-the-diff
loop (00), plan mode (01), subagents (02), worktrees and `/goal` (03).

| Branch | Topic |
|---|---|
| `claude_code_exercise/00` | One script — ask, edit, run, read the diff |
| `claude_code_exercise/01` | Logging & config — plan mode |
| `claude_code_exercise/02` | Monitor & schemes — subagents |
| `claude_code_exercise/03` | Best scheme & self-invented schemes — worktrees + `/goal` |

Check one out and read its `EXERCISE.md`:

```bash
git checkout claude_code_exercise/01
```

Setup: [uv](https://docs.astral.sh/uv/) manages deps, and runs need an
`OPEN_ROUTER_API_KEY` in `.env` (loaded automatically by python-dotenv).

```bash
uv sync
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

See `CLAUDE.md` for the repo conventions.
