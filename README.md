# SmartSuite Automations

Starter project for SmartSuite API scripts (moved out of Colab).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your API key and account ID to .env
```

Your API key lives only in `.env`, which is gitignored. Don't paste it into scripts or chat.

## Layout

- `smartsuite.py` – shared client (list/get/create/update records)
- `scripts/` – one file per automation
- `.env.example` – template for your credentials
- `.claude/settings.json` – Claude asks before every change and can't read `.env`

## Run

```bash
python scripts/example_list_records.py <table_id>
```

## Moving a Colab notebook in

1. In Colab: File → Download → Download .py
2. Save it in `scripts/`
3. Replace any hard-coded key with `import smartsuite` and the helper functions
