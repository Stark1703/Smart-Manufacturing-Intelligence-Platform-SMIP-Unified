import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class NotebookStructureTests(unittest.TestCase):
    def test_notebooks_are_valid_json_with_cell_metadata(self) -> None:
        notebooks = sorted((ROOT / "databricks").rglob("*.ipynb"))
        self.assertTrue(notebooks, "Expected Databricks notebooks to be present.")

        for path in notebooks:
            with self.subTest(notebook=path.relative_to(ROOT)):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(notebook.get("cells"), list)
                self.assertIsInstance(notebook.get("metadata"), dict)
                for cell in notebook["cells"]:
                    self.assertIn(cell.get("cell_type"), {"code", "markdown", "raw"})
                    self.assertIn("source", cell)
