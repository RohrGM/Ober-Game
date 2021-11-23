from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class IAnimatedSpriteEvents(ISubscriber, ABC):

    @abstractmethod
    def animation_finished_event(self, animation_name: str) -> None:
        pass

    @abstractmethod
    def locked_animation_event(self, state: bool) -> None:
        pass
