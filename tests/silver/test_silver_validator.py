import unittest
from datetime import UTC, datetime

from streaming.bronze.bronze_event import BronzeEvent
from streaming.silver.silver_validator import SilverValidator


class SilverValidatorTests(unittest.TestCase):
    def make_event(self, event: dict) -> BronzeEvent:
        return BronzeEvent(
            kafka_topic="manufacturing-events",
            kafka_partition=0,
            kafka_offset=1,
            ingestion_timestamp=datetime.now(UTC),
            event=event,
        )

    def test_accepts_a_supported_event(self) -> None:
        event = {
            "event_id": "event-1",
            "event_timestamp": datetime.now(UTC).isoformat(),
            "event_type": "OPERATION_COMPLETED",
            "event_version": "2.0",
            "plant_code": "PLANT-1",
            "payload": {"machine_id": "machine-1"},
        }
        validator = SilverValidator()

        self.assertTrue(validator.validate(self.make_event(event)))
        self.assertEqual(validator.errors, [])

    def test_reports_missing_fields_and_unsupported_version(self) -> None:
        validator = SilverValidator()

        self.assertFalse(
            validator.validate(
                self.make_event(
                    {
                        "event_id": 1,
                        "event_type": "UNKNOWN",
                        "event_version": "1.0",
                        "payload": [],
                    }
                )
            )
        )
        self.assertTrue(any("Missing required field" in error for error in validator.errors))
        self.assertTrue(any("Payload must be a dictionary" in error for error in validator.errors))
        self.assertTrue(any("event_id must be a string" in error for error in validator.errors))
        self.assertTrue(any("Unsupported event version" in error for error in validator.errors))
