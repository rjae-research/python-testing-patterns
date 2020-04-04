import pytest

from anti_patterns.closed_for_extension.message_broker import MessageBroker
from anti_patterns.closed_for_extension.message_producer import MessageProducer


def test_publish_must_produce_message():
    producer = MockMessageProducer()
    broker = MessageBroker(producer)
    assert 0 == producer._publish_called
    broker.publish("42")
    assert 1 == producer._publish_called


class MockMessageProducer(MessageProducer):

    def __init__(self):
        self._publish_called = 0

    def produce(self, message: str):
        super().produce(message)
        self._publish_called += 1

    @property
    def publish_called(self) -> int:
        return self._publish_called
