from typing import Type

import pyxel

from Interfaces.INode2D import INode2D
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2

MAX_DELAY = 6


class MenuScene(INode2D):

    def __init__(self, position: Vector2 = Vector2(0, 0)):
        self.__children_manager = ChildrenManager(self)
        self.__position = position
        self.__option = 0
        self.__delay = 0

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
        self.__delay -= 1
        if pyxel.btn(pyxel.KEY_UP) and self.__delay < 0:
            self.__delay = MAX_DELAY
            self.__option = 2 if self.__option == 0 else self.__option - 1

        elif pyxel.btn(pyxel.KEY_DOWN) and self.__delay < 0:
            self.__delay = MAX_DELAY
            self.__option = 0 if self.__option == 2 else self.__option + 1

        elif pyxel.btn(pyxel.KEY_ENTER):
            self.get_parent().change_scene("Level1")

    def draw(self):
        pyxel.rect(85, 45, 90, 70, 0)
        pyxel.text(113, 72, "CONTINUAR", 6 if self.__option == 0 else 1)
        pyxel.text(113, 80, " INICIAR ", 6 if self.__option == 1 else 1)
        pyxel.text(113, 88, "  SAIR ", 6 if self.__option == 2 else 1)


