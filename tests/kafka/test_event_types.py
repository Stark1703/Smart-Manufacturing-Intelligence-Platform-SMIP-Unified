import unittest

from streaming.events.event_types import EventType


class EventTypeTests(unittest.TestCase):
    def test_values_are_unique_and_match_enum_members(self) -> None:
        values = EventType.values()

        self.assertEqual(len(values), len(set(values)))
        self.assertEqual(values, [event.value for event in EventType])
        self.assertIn("OPERATION_COMPLETED", values)
