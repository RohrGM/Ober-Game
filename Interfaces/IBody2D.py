from abc import ABC, abstractmethod

from Interfaces.INode2D import INode2D
from Util.Vector2 import Vector2


class IBody2D(INode2D, ABC):

    @abstractmethod
    def add_body_on_collision_system(self, layer: int, mask: int, shape_size: Vector2):
        pass

    @abstractmethod
    def on_body_collision(self, body, pos_y):
        pass

