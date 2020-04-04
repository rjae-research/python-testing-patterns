import json

from anti_patterns.closed_for_extension.message_producer import MessageProducer

"""
Anti-pattern: Closed For Extension
* MessageBroker.__publish__ is closed for extension.
* MessageBroker.__get_message__ is closed for extension.
* MessageBroker.__get_partition__ is especially closed for extension given its static definition.
"""


class MessageBroker():

    def __init__(self, broker: MessageProducer):
        self._broker = broker

    @staticmethod
    def __get_partition__(value) -> int:
        return hash(value)

    def publish(self, value):
        partition: int = MessageBroker.__get_partition__(value)
        message: str = self.__get_message__(value)
        self.__publish__(partition, message)

    def __get_message__(self, value) -> str:
        return json.dumps(value)

    def __publish__(self, partition: int, message: str):
        self._broker.produce(message)
