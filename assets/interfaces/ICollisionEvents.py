from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class ICollisionEvents(ISubscriber, ABC):

    @abstractmethod
    def on_collision_body_event(self, agent: object, name: str, pos_y: int) -> None:
        pass