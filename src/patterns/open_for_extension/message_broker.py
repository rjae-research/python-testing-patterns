import json
from abc import ABC, abstractmethod

from patterns.open_for_extension.message_producer import MessageProducer


class MessageBrokerBase(ABC):

    def __init__(self, producer: MessageProducer):
        self._producer = producer

    def publish(self, value):
        partition: int = self._get_partition_(value)
        message: str = self._get_message_(value)
        self._publish_(partition, message)

    def _get_message_(self, value) -> str:
        return json.dumps(value)

    @abstractmethod
    def _get_partition_(self, value) -> int:
        return 0

    def _publish_(self, partition: int, message: str):
        self._producer.produce(message)


class MessageBroker(MessageBrokerBase):

    def __init__(self, producer: MessageProducer):
        super().__init__(producer)

    def _get_partition_(self, value) -> int:
        return abs(hash(value) + super()._get_partition_(value))
