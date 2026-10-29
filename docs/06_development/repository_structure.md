# Repository Structure

## Overview

The Unified repository contains the generator, streaming prototype, Databricks
implementation, and supporting analytics assets.

## Top-Level Structure

```text
Smart-Manufacturing-Intelligence-Platform-SMIP-Unified/
│
├── data/
├── databricks/
├── docs/
├── framework/
├── generator/
├── infrastructure/
├── powerbi/
├── sql/
├── streaming/
└── tests/
```

## Folder Descriptions

| Folder | Purpose |
|----------|---------|
| generator | Manufacturing simulator |
| framework | Shared utilities |
| databricks | Lakehouse notebooks |
| infrastructure | Local Kafka infrastructure |
| streaming | Event generation, Kafka integration, and Bronze/Silver processing |
| powerbi | Reports and themes |
| sql | SQL scripts and views |
| docs | Technical documentation |
| tests | Test resources |
| data | Generated datasets |

## Design Principles

- Separation of concerns
- Modular architecture
- Layered processing
- Reusable components

## Related Documentation

- Coding Guidelines
- Project Overview