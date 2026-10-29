# Tests

The automated unit tests use Python's standard-library `unittest` runner. They
exercise the JSONL Bronze/Silver readers, Silver transformation and validation,
Silver writing, event-type definitions, local Markdown links, and notebook JSON
structure. Tests use temporary directories and do not require or modify the
checked-in sample datasets.

Run the complete suite from the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The suite is also run by [GitHub Actions](../.github/workflows/ci.yml) for pushes
and pull requests.

## Manual service examples

Kafka examples are kept outside the test suite under [`examples/kafka/`](../examples/kafka/).
Install the optional client with `python -m pip install -r requirements-kafka.txt`.
Start the broker with
`docker compose -f infrastructure/kafka/docker-compose.yml up -d`, then run
`python -m examples.kafka.consume_events` and
`python -m examples.kafka.produce_event` in separate terminals. Stop it with
`docker compose -f infrastructure/kafka/docker-compose.yml down`. These scripts
are not run by unit-test discovery.

Databricks notebook and Power BI validation requires their respective external
services and is not covered by the local unit-test job.
