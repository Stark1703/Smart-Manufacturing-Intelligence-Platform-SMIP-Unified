# SMIP documentation

This documentation covers the unified repository: the manufacturing data generator,
event-streaming prototype, Databricks Lakehouse notebooks, SQL assets, and Power BI
materials. The two source branches have been integrated; these components are no
longer documented as separate repositories.

## Start here

1. [Project overview](01_overview/README.md)
2. [Architecture](02_architecture/README.md)
3. [Data model](03_data_model/README.md)
4. [Data engineering](04_data_engineering/README.md)
5. [Business intelligence](05_business_intelligence/README.md)
6. [User guide](06_user_guide/README.md)
7. [Development guide](07_development/README.md)

The [repository root README](../README.md) provides the short project overview and
quick start. The [branch integration notes](merge-plan.md) record the history of the
unification work; they are not deployment instructions.

## Documentation map

| Area | Canonical section | Contents |
|---|---|---|
| Overview | [`01_overview/`](01_overview/README.md) | Business problem, scope, manufacturing workflow, project goals |
| Architecture | [`02_architecture/`](02_architecture/README.md) | System, Lakehouse, pipeline, Medallion Architecture, technology stack |
| Data model | [`03_data_model/`](03_data_model/README.md) | Event model, business keys, dimensions, facts, data lineage |
| Data engineering | [`04_data_engineering/`](04_data_engineering/README.md) | Bronze/Silver/Gold processing, dimensions, facts, execution |
| Business intelligence | [`05_business_intelligence/`](05_business_intelligence/README.md) | KPIs, dashboards, SQL analytics |
| User guide | [`06_user_guide/`](06_user_guide/README.md) | Setup, execution, dashboard usage, troubleshooting |
| Development | [`07_development/`](07_development/README.md) | Repository structure, branch history, decisions, roadmap |
| Diagrams and screenshots | [`08_images/`](08_images/) | Architecture, dashboards, schemas, lineage |
| V2 roadmap | [`08_v2.0/`](08_v2.0/) | Proposed streaming, API, predictive maintenance, and CI/CD increments |

## Supplemental material

The merge brought in additional documents under
[`02_data_model/`](02_data_model/README.md),
[`03_data_engineering/`](03_data_engineering/README.md),
[`04_business_intelligence/`](04_business_intelligence/README.md),
[`05_user_guide/`](05_user_guide/README.md),
[`06_development/`](06_development/README.md), and
[`07_images/`](07_images/README.md). These are supplemental source-branch
documents retained for reference. Prefer the canonical sections above when both
areas cover the same topic.

## Technology scope

The repository includes Python-based data generation and streaming code, Databricks
notebooks using Spark/Delta Lake, SQL assets, and Power BI reports. Some components
require external services or platform-specific setup; see the [environment setup guide](06_user_guide/environment_setup.md)
and [Databricks notebook guide](../databricks/README.md) before running them.