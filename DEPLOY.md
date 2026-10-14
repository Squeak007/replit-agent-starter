# Deploy to Replit (5 minutes)

## Option 1: Interactive agent (default)

1. Fork this template to your Replit account.
2. Open the **Secrets** tab (padlock icon in the left sidebar).
3. Add either `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` (whichever you want to use).
4. Hit the big green **Run** button. You'll land in the chat agent.

## Option 2: Run an example

In the Shell tab:

```bash
python examples/summarize_url.py https://thefloortimecenter.com
```

Or any of the other examples under `examples/`.

## Option 3: Scheduled Deployment (cron agent)

Perfect for daily digests, price watchers, scrapers.

1. In Replit, click **Deploy** → **Scheduled**.
2. Set schedule: `0 9 * * *` (daily at 9am) or whatever cadence you want.
3. Run command: `python examples/cron_agent.py`
4. Add env vars under Secrets:
   - `ANTHROPIC_API_KEY` (or `OPENAI_API_KEY`)
   - `TASK` (the thing you want it to do each run)
5. Deploy.

Replit will run your agent on schedule. Output lands in `runs/` inside your repl.

## Option 4: Autoscale Deployment (web agent)

If you build an HTTP wrapper around `agent.py` (e.g., with FastAPI), Replit Autoscale will host it.

1. Click **Deploy** → **Autoscale**.
2. Build command: `pip install -r requirements.txt`
3. Run command: `python your_server.py`
4. Add API keys in Secrets.

## Troubleshooting

- **"No API key" error** → double-check Secrets tab. Env vars are case-sensitive.
- **Import errors** → run `pip install -r requirements.txt` manually in Shell.
- **Rate limits** → add retries in `providers.py` or lower your usage.
- **Can't fork?** → make sure you have a Replit account at replit.com.

Still stuck? Reply to your Gumroad receipt — I respond within 24h.
