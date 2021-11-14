from Util.ChildrenManager import ChildrenManager
from Interfaces.INode2D import INode2D
from Util.Vector2 import Vector2
from typing import Type
import pyxel


class HitMark(INode2D):

    def __init__(self, image: str, pos_y: int, position: Vector2 = Vector2(0, 0)) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__position = position
        self.__image = image
        self.__pos_y = pos_y
        self.__life = 5

    def add_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.add_child(child)

    def remove_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.remove_child(child)

    def add_parent(self, parent: Type[INode2D]) -> None:
        self.__children_manager.add_parent(parent)

    def get_parent(self) -> Type[INode2D]:
        return self.__children_manager.get_parent()

    def remove_parent(self) -> None:
        self.__children_manager.remove_parent()

    def get_children(self) -> list:
        return self.__children_manager.get_children()

    def set_children(self, children: list) -> None:
        self.__children_manager.set_children(children)

    def get_position(self) -> Vector2:
        if self.get_parent() is None:
            return self.__position
        return Vector2.sum_vector(self.get_parent().get_position(), self.__position)

    def set_position(self, position: Vector2):
        self.__position = position

    def queue_free(self) -> None:
        if self.get_parent() is not None:
            self.get_parent().remove_child(self)

    def update(self) -> None:
        self.__life -= 1
        if self.__life < 0:
            self.queue_free()

    def draw(self) -> None:
        pyxel.blt(self.get_position().x + 3,
                  self.get_position().y + self.__pos_y - 3, 0, 232 if self.__image == "head" else 225, 25, 5, 6,
                  pyxel.COLOR_PURPLE)
