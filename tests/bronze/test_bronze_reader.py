import json
import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path

from streaming.bronze.bronze_reader import BronzeReader


class BronzeReaderTests(unittest.TestCase):
    def test_reads_jsonl_events_and_counts_them(self) -> None:
        event = {
            "event_id": "event-1",
            "event_type": "OPERATION_COMPLETED",
        }
        record = {
            "kafka_topic": "manufacturing-events",
            "kafka_partition": 2,
            "kafka_offset": 17,
            "ingestion_timestamp": datetime.now(UTC).isoformat(),
            "event": event,
        }

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text(json.dumps(record) + "\n", encoding="utf-8")
            reader = BronzeReader(path)

            events = list(reader.read_events())

            self.assertEqual(reader.path, path)
            self.assertEqual(reader.count(), 1)
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].event, event)
            self.assertEqual(events[0].kafka_partition, 2)
            self.assertEqual(events[0].kafka_offset, 17)

    def test_missing_file_is_an_empty_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            reader = BronzeReader(Path(directory) / "missing.jsonl")

            self.assertEqual(reader.read_all(), [])
            self.assertEqual(reader.count(), 0)
