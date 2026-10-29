# Running the data workflows

SMIP includes local Python components and two Databricks notebook processing
paths. They have different inputs and output models; select one path and verify
its expected schema and storage targets before execution.

## Local checks

From the repository root, run the dependency-free unit tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The Kafka producer and consumer examples require the optional Kafka client and a
running broker. Start the local broker with
[`infrastructure/kafka/docker-compose.yml`](../../infrastructure/kafka/docker-compose.yml),
then follow the usage notes in [`tests/README.md`](../../tests/README.md).

## Databricks notebooks

Follow the setup requirements in [environment setup](environment_setup.md), then
choose one path documented in the [Databricks guide](../../databricks/README.md):

- **Event-based Lakehouse:** setup, event-based Bronze and Silver notebooks,
  dimensions, facts, Gold KPIs, dashboard assets, then validation.
- **Transactional CSV:** generate CSV data, ingest master and transactional
  records, build dimensions and facts, run Gold summaries, then SQL/Power BI
  preparation.

Notebook names and subdirectories are not a single globally ordered list: the
repository retains similarly numbered notebooks from both source branches. Use
the path-specific order, inspect each notebook's configured catalog/schema and
input/output paths, and do not assume all assets can be run together.

The repository contains declarative pipeline notebook code but does not include
a deployment bundle or workspace-specific pipeline/job definition. Configure
that orchestration in Databricks and review its dependencies before execution.

## Validation

- Run the repository's local unit tests before changing Python components.
- Use `databricks/notebooks/07_validation/01_pipeline_validation.py.ipynb` for
  the Databricks event-based path after its upstream tables are available.
- Confirm the selected path's expected source files, tables, and dashboard data
  in the target workspace; sample counts in older documents are not universal
  acceptance thresholds.
