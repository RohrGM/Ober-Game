from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class IBarricadeEvents(ISubscriber, ABC):

    @abstractmethod
    def dead_event(self, agent: object):
        pass
