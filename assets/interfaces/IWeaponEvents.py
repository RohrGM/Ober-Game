from abc import ABC, abstractmethod
from .ISubscriber import ISubscriber


class IWeaponEvents(ISubscriber, ABC):

    @abstractmethod
    def shoot_event(self, anim: str) -> None:
        pass

    @abstractmethod
    def reload_event(self, anim: str) -> None:
        pass

    @abstractmethod
    def special_event(self, anim: str) -> None:
        pass
