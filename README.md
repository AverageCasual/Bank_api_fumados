# Banking API Prototype

A Python and FastAPI exercise for managing sample accounts and balances. All data is held in memory and resets when the server stops.

## Run locally

Create and activate a Python virtual environment, then run:

```bash
python -m pip install -r requirements.txt
python -m uvicorn Bank:app --host 127.0.0.1 --port 8000
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to try the API with sample data.

| Method | Route | Purpose |
| --- | --- | --- |
| POST | `/Register` | Create an account |
| POST | `/Login` | Check credentials |
| PUT | `/Modify` | Change a password |
| DELETE | `/Delete` | Delete an account |
| POST | `/Balance` | Read a balance |
| POST | `/Add_Balance` | Add funds to a sample balance |
| POST | `/Withdrawal` | Subtract funds from a sample balance |

## What this project covers

- Defining HTTP routes with FastAPI.
- Updating Python dictionaries through API requests.
- Returning status codes for duplicate accounts and unauthorized operations.

## Limitations

This is a local prototype with no database or transaction handling. Credentials are plain text and passed as request parameters. Input validation is incomplete, including the check for non-positive withdrawals. It needs further work before handling real users or financial data.
