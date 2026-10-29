# User guide

This guide covers local development and the Databricks-hosted analytics
workflows. The notebooks are source assets; a Databricks workspace, cloud
resources, access permissions, and any required pipeline/job configuration must
be supplied separately.

## Recommended order

1. [Install and run local tests](installation.md).
2. [Prepare a Databricks workspace](environment_setup.md) if you are using the
   Lakehouse notebooks.
3. Choose one of the [documented notebook processing paths](../../databricks/README.md).
4. [Run and validate the selected notebooks](running_the_pipeline.md).
5. Review [dashboard usage](dashboard_usage.md) and
   [troubleshooting](troubleshooting.md).

Do not run the transactional-CSV and event-based notebook paths together against
the same catalog without first reconciling their inputs, table names, and write
modes.
