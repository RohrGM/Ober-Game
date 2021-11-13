from typing import Type

import pyxel

from Interfaces.INode2D import INode2D
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2


class PlayerSpecial(INode2D):

    def __init__(self, position: Vector2 = Vector2(0, 0)):
        self.__children_manager = ChildrenManager(self)
        self.__position = position

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

    def set_children(self, children: list) -> None:
        self.__children_manager.set_children(children)

    def get_position(self) -> Vector2:
        if self.__children_manager.get_parent() is None:
            return self.__position
        return Vector2.sum_vector(self.__children_manager.get_parent().get_position(), self.__position)

    def set_position(self, position: Vector2):
        self.__position = position

    def queue_free(self) -> None:
        if self.__children_manager.get_parent() is not None:
            self.__children_manager.get_parent().remove_child(self)

    def update(self):
        pass

    def draw(self):
        pyxel.rect(15, 10, 52, 4, 7 if self.__children_manager.get_parent().get_special() < 50 else pyxel.frame_count % 16)
        pyxel.rect(16, 11, self.__children_manager.get_parent().get_special(), 2, 2)
        pyxel.blt(2, 5, 0, 232, 7, 11, 12, pyxel.COLOR_PURPLE)