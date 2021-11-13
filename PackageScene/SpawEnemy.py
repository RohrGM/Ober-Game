from Util.ChildrenManager import ChildrenManager
from Interfaces.INode2D import INode2D
from PackageScene.Enemy import Enemy
from Util.Vector2 import Vector2
from random import randrange
from typing import Type
import pyxel


class SpawEnemy(INode2D):

    def __init__(self, position: Vector2 = Vector2(0, 0)) -> None:
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

    def update(self) -> None:
        if pyxel.frame_count % randrange(40, 70) == 0:
            self.get_parent().add_child(Enemy(position=Vector2(randrange(270, 350), randrange(70, 110))))

    def draw(self) -> None:
        pass
