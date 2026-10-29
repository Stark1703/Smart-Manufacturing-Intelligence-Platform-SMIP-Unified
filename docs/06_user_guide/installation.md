# Local installation

This guide covers the Python components. Databricks workspace setup is described
in [environment setup](environment_setup.md).

## Prerequisites

- Python 3.13 or newer.
- Git.
- Docker Compose only if you intend to run the local Kafka broker.

## Clone and prepare a virtual environment

```bash
git clone https://github.com/Stark1703/Smart-Manufacturing-Intelligence-Platform-SMIP-Unified.git
cd Smart-Manufacturing-Intelligence-Platform-SMIP-Unified
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS or Linux
source .venv/bin/activate
```

## Install dependencies

Install the project's runtime dependencies only for the components you plan to
run; `requirements.txt` includes Spark/Delta packages and may take time to
install:

```bash
python -m pip install -r requirements.txt
```

The Kafka examples use an optional dependency:

```bash
python -m pip install -r requirements-kafka.txt
```

## Run local tests

The unit tests use the Python standard library and do not require installing the
runtime dependencies:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

To run the Kafka examples, start the broker in
[`infrastructure/kafka/`](../../infrastructure/kafka/), then run:

```bash
python -m examples.kafka.consume_events
python -m examples.kafka.produce_event
```

Databricks notebooks and Power BI reports require their respective external
services. See the [Databricks environment guide](environment_setup.md).
