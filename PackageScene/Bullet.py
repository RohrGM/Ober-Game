from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from Util.Vector2 import Vector2
from Util.ChildrenManager import ChildrenManager
from typing import Type


class Bullet(IBody2D):

    def __int__(self, children_manager: ChildrenManager, position: Vector2):
        self.__children_manager = children_manager
        self.__position = position

    def add_body_on_collision_system(self, layer: int, mask: int, shape_size: Vector2):
        pass

    def on_body_collision(self, body, pos_y):
        pass

    def add_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.add_child(child)

    def remove_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.remove_child(child)

    def add_parent(self, parent: Type[INode2D]) -> None:
        self.__children_manager.add_parent(parent)

    def remove_parent(self) -> None:
        self.__children_manager.remove_parent()

    def set_children(self, children: list) -> None:
        self.__children_manager.set_children(children)

    def get_position(self) -> Vector2:
        return Vector2.sum_vector(self.__children_manager.get_parent(), self.__position)

    def queue_free(self) -> None:
        if self.__children_manager.get_parent() is not None:
            self.__children_manager.get_parent().remove_child(self)
