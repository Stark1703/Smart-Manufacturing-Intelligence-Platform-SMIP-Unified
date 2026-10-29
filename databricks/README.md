# Databricks assets

This directory contains two notebook-based processing paths inherited from the
source branches. They overlap in table names and are not one combined workflow.
Choose the path that matches the dataset and expected outputs; do not run both
against the same catalog without reviewing their schemas and write modes.

## Event-based Lakehouse path

This path processes JSON manufacturing events through Lakeflow Declarative
Pipelines and builds a Databricks SQL dashboard.

1. Run the notebooks in `notebooks/00_setup/` to prepare and validate the workspace.
2. Configure a Lakeflow pipeline with the event-based notebooks in
   `notebooks/01_bronze/` and `notebooks/02_silver/`.
3. Add the event-model dimensions from `notebooks/03_dimensions/`, facts from
   `notebooks/04_facts/`, and KPI tables from `notebooks/05_gold/`.
4. Review the dashboard assets in `notebooks/06_sql_dashboard/`.
5. Run `notebooks/07_validation/01_pipeline_validation.py.ipynb`.

The pipeline definition and workspace-specific catalog, schema, volume, and
permissions are not provisioned by this repository. Configure them in Databricks
before running the declarative notebooks.

## Transactional CSV path

This path generates the master and transactional CSV datasets and processes them
through the earlier Databricks model:

1. Generate data with `notebooks/05_data_generation/01_run_smip.ipynb`.
2. Ingest master and transactional data with the relevant notebooks in
   `notebooks/01_bronze/`.
3. Run dimensions and facts under `notebooks/02_silver/dimensions/` and
   `notebooks/02_silver/facts/`.
4. Run the summaries in `notebooks/03_gold/`, then SQL in
   `notebooks/04_sql/01_views.sql`.
5. Use the export notebooks in `notebooks/06_powerbi/` when preparing Power BI
   data.

The `02_silver` and `03_gold` folders also contain notebooks from the event-based
path. Check notebook inputs and target tables before mixing assets from the two
paths.

## Notebooks are not local Python modules

The `.ipynb` and `.py.ipynb` files are intended for Databricks runtimes. Their
Spark, Delta, Unity Catalog, and Lakeflow dependencies are not exercised by the
local unit-test suite. See the [user guide](../docs/06_user_guide/README.md) for
environment setup and [the documentation index](../docs/README.md) for project
architecture.
