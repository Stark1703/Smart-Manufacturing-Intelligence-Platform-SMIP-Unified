import copy
import unittest
from datetime import UTC, datetime

from streaming.bronze.bronze_event import BronzeEvent
from streaming.silver.silver_transformer import SilverTransformer


class SilverTransformerTests(unittest.TestCase):
    def test_normalizes_nested_strings_without_mutating_bronze_event(self) -> None:
        event = {
            "event_id": " event-1 ",
            "payload": {"machine_id": " machine-1 ", "optional": " "},
            "items": [{"name": " item-1 "}],
        }
        original = copy.deepcopy(event)
        bronze_event = BronzeEvent(
            kafka_topic="manufacturing-events",
            kafka_partition=0,
            kafka_offset=1,
            ingestion_timestamp=datetime.now(UTC),
            event=event,
        )

        silver_event = SilverTransformer().transform(bronze_event)

        self.assertEqual(silver_event.event["event_id"], "event-1")
        self.assertEqual(silver_event.event["payload"]["machine_id"], "machine-1")
        self.assertIsNone(silver_event.event["payload"]["optional"])
        self.assertEqual(silver_event.event["items"][0]["name"], "item-1")
        self.assertEqual(bronze_event.event, original)
