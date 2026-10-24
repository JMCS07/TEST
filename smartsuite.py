"""Shared SmartSuite API client. Reads credentials from .env."""
import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://app.smartsuite.com/api/v1"


def _headers():
    try:
        return {
            "Authorization": f"Token {os.environ['SMARTSUITE_API_KEY']}",
            "Account-Id": os.environ["SMARTSUITE_ACCOUNT_ID"],
            "Content-Type": "application/json",
        }
    except KeyError as e:
        raise SystemExit(f"Missing {e.args[0]} in .env (see .env.example)")


def _request(method, path, **kwargs):
    resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(), timeout=30, **kwargs)
    resp.raise_for_status()
    return resp.json() if resp.content else None


def list_records(table_id, limit=100, offset=0, filter=None):
    body = {"filter": filter} if filter else {}
    return _request("POST", f"/applications/{table_id}/records/list/",
                    params={"limit": limit, "offset": offset}, json=body)


def get_record(table_id, record_id):
    return _request("GET", f"/applications/{table_id}/records/{record_id}/")


def create_record(table_id, fields):
    return _request("POST", f"/applications/{table_id}/records/", json=fields)


def update_record(table_id, record_id, fields):
    return _request("PATCH", f"/applications/{table_id}/records/{record_id}/", json=fields)
