import json
import tempfile
import unittest
from pathlib import Path

from streaming.silver.silver_reader import SilverReader


class SilverReaderTests(unittest.TestCase):
    def test_reads_jsonl_and_skips_blank_lines(self) -> None:
        events = [{"event": {"event_id": "event-1"}}, {"event": {"event_id": "event-2"}}]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text(
                f"{json.dumps(events[0])}\n\n{json.dumps(events[1])}\n",
                encoding="utf-8",
            )
            reader = SilverReader(path)

            self.assertEqual(reader.read_all(), events)
            self.assertEqual(reader.count(), 2)

    def test_missing_file_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            reader = SilverReader(Path(directory) / "missing.jsonl")

            self.assertEqual(reader.read_all(), [])
