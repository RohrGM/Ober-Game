from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class IBulletEvents(ISubscriber, ABC):

    @abstractmethod
    def critical_event(self, damage: float) -> None:
        pass

    @abstractmethod
    def dead_event(self, bullet: object) -> None:
        pass
