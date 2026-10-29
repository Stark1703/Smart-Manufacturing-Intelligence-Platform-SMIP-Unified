# Databricks environment setup

The Databricks notebooks require a workspace configured for the APIs and
libraries used by the selected processing path. This repository does not create
cloud resources, configure identity, or provision a Lakeflow pipeline.

## Prerequisites

- A Databricks workspace with a compatible Spark/Delta runtime.
- Unity Catalog access if the selected notebooks use catalogs, schemas, or volumes.
- Permission to create or write the tables and volumes used by the notebooks.
- A SQL Warehouse for the SQL dashboard or Power BI workflows.
- Git access to this repository, or an uploaded copy of the required notebooks.

Use your organization's approved workspace, compute, identity, and data-governance
settings. Do not commit access tokens, hostnames containing secrets, or
environment-specific credentials.

## Prepare the workspace

1. Connect the Unified repository to Databricks Repos or import the required
   notebooks.
2. Review and run the notebooks in `databricks/notebooks/00_setup/` in order.
   The setup notebooks cover workspace, catalog, schema, volume, and validation
   tasks; confirm the target names and permissions before execution.
3. Select either the [event-based Lakehouse path](../../databricks/README.md#event-based-lakehouse-path)
   or the [transactional CSV path](../../databricks/README.md#transactional-csv-path).
4. Configure the relevant Lakeflow pipeline or notebook job in the workspace.
   No workspace-specific pipeline/job definition is committed here.
5. Confirm that the expected input data is available at the locations configured
   in the notebooks before starting processing.

## Local Python and Kafka

The local Python components have a separate setup path. See
[installation](installation.md) and the [Kafka example requirements](../../requirements-kafka.txt).
Local unit tests do not require a Databricks workspace or a Kafka broker.
