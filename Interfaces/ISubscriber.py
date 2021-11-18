from abc import ABC, abstractmethod


class ISubscriber(ABC):

    @abstractmethod
    def add_subscriber(self, func, event_name) -> None:
        pass

    @abstractmethod
    def remove_subscriber(self, func, event_name) -> None:
        pass
