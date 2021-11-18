from abc import ABC, abstractmethod


class IAnimatedSpriteEvents(ABC):

    @abstractmethod
    def animation_finish_event(self, animation_name: str) -> None:
        pass

    @abstractmethod
    def locked_animation_event(self, state: bool) -> None:
        pass
