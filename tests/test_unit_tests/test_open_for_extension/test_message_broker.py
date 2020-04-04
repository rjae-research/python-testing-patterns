import pytest

from patterns.open_for_extension.message_broker import MessageBroker
from patterns.open_for_extension.message_producer import MessageProducer


def test_publish_must_produce_message():
    producer = MockMessageProducer()
    broker = MockMessageBroker(producer)
    assert 0 == producer._publish_called
    broker.publish("42")
    assert 1 == producer._publish_called


def test_publish_must_produce_message_on_expected_partition():
    producer = MockMessageProducer()
    broker = MockMessageBroker(producer)
    assert 0 == len(broker.messages)
    broker.publish("42")
    partition, value = broker.messages[0]
    assert "42" == value
    expected = abs(hash(value))
    assert expected == partition


class MockMessageBroker(MessageBroker):

    def __init__(self, producer: MessageProducer):
        super().__init__(producer)
        self._messages = []

    def _get_partition_(self, value) -> int:
        partition = super()._get_partition_(value)
        self._messages.append((partition, value))
        return partition

    @property
    def messages(self) -> int:
        return self._messages


class MockMessageProducer(MessageProducer):

    def __init__(self):
        self._publish_called = 0

    def produce(self, message: str):
        super().produce(message)
        self._publish_called += 1

    @property
    def publish_called(self) -> int:
        return self._publish_called
