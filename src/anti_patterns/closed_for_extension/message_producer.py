from abc import ABC, abstractmethod


class MessageProducer(ABC):

    @abstractmethod
    def produce(self, message: str):
        pass
