from abc import ABC, abstractmethod


class IOnPyxel(ABC):

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
