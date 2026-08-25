# AGENTS.md

## Cursor Cloud specific instructions

This repository is a Python (3.12) API test suite that exercises the public
cat-fact API using `pytest`, `requests`, `pydantic`, and `allure-pytest`. There
is no server/build step — the "application" is the pytest suite itself.

### Environment / running

- Dependencies are installed into a virtualenv at `venv/` by the startup update
  script. Use the venv interpreter directly (no need to activate):
  `./venv/bin/python -m pytest`.
- Run the suite with the command documented in `README.md`:
  `./venv/bin/python -m pytest --alluredir=reports/allure-results`.
- `allure serve reports/allure-results` (from the README) requires the standalone
  Allure CLI (a Java tool) which is NOT installed and NOT needed to run tests —
  only to render the HTML report. Skip it unless a report UI is explicitly needed.

### Important caveat: the upstream API is offline

- The tests hit `https://cat-fact.herokuapp.com/` (see `utils/config/config.yaml`).
  Heroku shut down its free tier, so this host now returns **HTTP 503
  "Application Error"**. As a result, `ApiGetRandomFact.get()` /
  `ApiGetFactByFactID.get()` return `None` and all 5 tests currently FAIL with
  `AttributeError: 'NoneType' object has no attribute 'status_code'`.
- These failures are an external-dependency outage, NOT an environment/setup
  problem. Do not "fix" them by editing app code unless explicitly asked; the
  correct fix is a live endpoint in `config.yaml` or mocking the HTTP layer.
- To validate the internal pipeline (requests → pydantic models → validators)
  without the dead host, mock `requests.get` (e.g. `unittest.mock.patch` on
  `models.facts.api_get_random_fact.requests.get`) to return a 200 response with
  a cat-fact JSON payload. This passes end-to-end.

### Lint

- No linter (ruff/flake8/black config) is configured in this repo.
