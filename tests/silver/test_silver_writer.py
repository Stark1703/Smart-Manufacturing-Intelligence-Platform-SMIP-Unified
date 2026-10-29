import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path

from streaming.silver.silver_event import SilverEvent
from streaming.silver.silver_reader import SilverReader
from streaming.silver.silver_storage import SilverStorage
from streaming.silver.silver_writer import SilverWriter


class SilverWriterTests(unittest.TestCase):
    def test_writes_events_to_the_configured_directory(self) -> None:
        event = SilverEvent(
            event={"event_id": "event-1"},
            bronze_ingestion_timestamp=datetime.now(UTC),
            silver_processing_timestamp=datetime.now(UTC),
        )

        with tempfile.TemporaryDirectory() as directory:
            storage = SilverStorage(output_directory=directory)
            writer = SilverWriter(storage=storage)

            writer.write_event(event)

            self.assertEqual(writer.path, Path(directory) / "manufacturing_events.jsonl")
            stored = SilverReader(writer.path).read_all()
            self.assertEqual(len(stored), 1)
            self.assertEqual(stored[0]["event"], event.event)
