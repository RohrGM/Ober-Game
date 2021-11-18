from abc import ABC, abstractmethod


class IWeaponEvents(ABC):

    @abstractmethod
    def shoot_event(self) -> None:
        pass

    @abstractmethod
    def reload_event(self) -> None:
        pass
