from abc import ABC, abstractmethod
from Util.Vector2 import Vector2


class INode2D(ABC):

    @abstractmethod
    def add_child(self, child: object) -> None:
        pass

    @abstractmethod
    def remove_child(self, child: object) -> None:
        pass

    @abstractmethod
    def add_parent(self, parent: object) -> None:
        pass

    @abstractmethod
    def get_parent(self) -> object:
        pass

    @abstractmethod
    def remove_parent(self) -> None:
        pass

    @abstractmethod
    def set_children(self, children: list) -> None:
        pass

    @abstractmethod
    def get_position(self) -> Vector2:
        pass

    @abstractmethod
    def set_position(self, position: Vector2):
        pass

    @abstractmethod
    def queue_free(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
