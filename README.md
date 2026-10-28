# Flask API Assignment

This is my basic Flask app for the Python/API assignment. It has two endpoints, `/hello` (GET) and `/sum` (POST), plus tests for both using pytest.

## What it does

- `GET /hello` sends back a JSON greeting. If you add `?name=Alice` it says hello to Alice, otherwise it says hello to World.
- `POST /sum` takes a JSON list of numbers and returns the total. If the input is bad (missing field, not a list, non-numbers, or invalid JSON) it returns a 400 error with a message.

## Setup

I'm on Windows, so these are the Windows commands. On Mac/Linux use `source venv/bin/activate` to activate instead.

```
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install Flask pytest
```

## Running the server

```
python app.py
```

The server starts on http://127.0.0.1:5000. When I opened `/hello` in my browser it worked and the terminal showed `GET /hello` with a 200.

To test `/sum` I used PowerShell in a second window:

```
Invoke-RestMethod -Uri http://127.0.0.1:5000/sum -Method Post -ContentType "application/json" -Body '{"numbers": [1,2,3]}'
```

That returned a sum of 6. When I sent `{"values": [1,2]}` (no `numbers` field) I got a 400, and I got a 400 again with `{"numbers": [1,"two"]}`.

## Running the tests

```
pytest test_app.py
```

All 7 tests passed. They cover `/hello` with and without a name, `/sum` with valid numbers, and `/sum` with a missing field, a non-list value, a non-numeric item, and invalid JSON (all of those should give a 400).

## Files

- `app.py` - the Flask app
- `test_app.py` - the pytest tests
- `README.md` - this file
