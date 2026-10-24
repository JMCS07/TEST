"""Example: print the first 10 records of a table.

Usage: python scripts/example_list_records.py <table_id>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import smartsuite  # noqa: E402

if len(sys.argv) != 2:
    raise SystemExit(__doc__)

data = smartsuite.list_records(sys.argv[1], limit=10)
for item in data.get("items", []):
    print(item["id"], item.get("title"))
