from abc import ABC, abstractmethod

from Interfaces.INode2D import INode2D
from Util.Vector2 import Vector2


class IBody2D(INode2D, ABC):

    @abstractmethod
    def on_body_collision(self, body: object, pos_y: int) -> None:
        pass

    @abstractmethod
    def get_rect_size(self) -> Vector2:
        pass

