
# Contributing

Thank you for helping improve SMIP. Changes should keep the Python generator,
streaming prototype, Databricks assets, and documentation consistent.

## Development setup

1. Use Python 3.13 or newer.
2. Create and activate a virtual environment.
3. Install project dependencies with `python -m pip install -r requirements.txt`
   when working on components that need those dependencies.
4. Run the dependency-free unit tests from the repository root:

   ```bash
   python -m unittest discover -s tests -p "test_*.py" -v
   ```

## Pull requests

- Keep changes focused and explain the user-visible or operational impact.
- Update the relevant documentation when behavior, configuration, or setup changes.
- Add or update tests for behavior changes; do not make automated tests depend on
  a live Kafka broker, Databricks workspace, or checked-in data being writable.
- Do not commit credentials, local environment files, generated datasets, or
  notebook execution output.
- Confirm Python compilation and the unit-test suite pass before requesting review.

The GitHub Actions workflow runs the same local checks on pushes and pull requests.
