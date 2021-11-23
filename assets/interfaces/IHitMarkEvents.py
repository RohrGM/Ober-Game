from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class IHitMarkEvents(ISubscriber, ABC):

    @abstractmethod
    def dead_event(self, agent: object) -> None:
        pass
