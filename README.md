# The Replit Agent Starter Kit

**Ship your first AI agent today, not next quarter.**

A production-ready Replit template with everything you need to build agents that actually *do things* — summarize URLs, scrape sites, write content, run on a schedule — using OpenAI or Anthropic.

Battle-tested. Opinionated. Shippable.

---

## 🛒 Get the kit — $19

The full ZIP with all source, examples, and the Replit one-click template:

- **Direct checkout (lowest fee):** [buy.stripe.com/00wbJ3eAl1KGa0fdJT18c00](https://buy.stripe.com/00wbJ3eAl1KGa0fdJT18c00)
- **Gumroad (same price, their checkout):** [squeakco.gumroad.com/l/replit-agent-starter-kit](https://squeakco.gumroad.com/l/replit-agent-starter-kit)

The source in this repo is MIT-licensed and free to read / fork. Paying gets you the packaged kit (one-click Replit import, 5 example agents configured, support, and future updates).

---

## What's inside

- **`agent.py`** — a clean agent loop with tool-calling
- **`providers.py`** — one API for OpenAI *and* Anthropic (switch with one env var)
- **`tools/`** — ready-to-use tools: HTTP fetch, URL summarizer, file read/write, bash exec, scheduled runner
- **`prompts/`** — 5 battle-tested system prompts for common agent patterns
- **`examples/`** — 5 working agents you can fork and modify:
  1. `summarize_url.py` — paste a URL, get a summary
  2. `scrape_and_notify.py` — scrape a page, email on change
  3. `writing_assistant.py` — polish drafts, keep your voice
  4. `cron_agent.py` — run on a schedule via Replit Deployments
  5. `chat_cli.py` — minimal terminal chat UI
- **`.replit`** — one-click run on Replit
- **`.env.example`** — API key template
- **`DEPLOY.md`** — ship to Replit Autoscale in 5 minutes

## Quickstart (10 minutes)

1. **Click "Run on Replit"** → forks the template to your account
2. **Set your API key** → open the Secrets tab, add `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`
3. **Run `python agent.py`** → say hi to your first agent
4. **Modify an example** → `examples/summarize_url.py` is the fastest to extend

## Why this kit?

The internet is full of "hello world" agent demos. This kit is different:

- **Replit-native** — no `pip install` dance, no venv hell. Fork → run.
- **Multi-provider** — swap OpenAI/Anthropic with one line. No vendor lock-in.
- **Shipped, not demoed** — the examples do real work (scrape, summarize, cron) you can deploy today.
- **By a dev who ships** — built by Squeak Co, same shop behind production Replit apps.

## Support

Questions? Reply to your purchase receipt — I respond within 24h.

## License

MIT — fork it, sell it, ship it. Just don't claim you wrote it.

---

Built by [Squeak Co](https://squeakco.substack.com). More tools: [github.com/squeak007](https://github.com/squeak007).
