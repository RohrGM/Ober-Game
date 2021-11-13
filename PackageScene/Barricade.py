from typing import Type

import pyxel

from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from Util.ChildrenManager import ChildrenManager
from Util.CollisionBody import CollisionBody
from Util.Vector2 import Vector2


class Barricade(IBody2D):

    def __init__(self, position: Vector2 = Vector2(40, 50), rect_size: Vector2 = Vector2(32, 96),
                 name: str = "Barricade") -> None:
        self.__children_manager = ChildrenManager(self)
        self.__collision_body = CollisionBody(agent=self, layer=2, mask=3, rect_size=rect_size)
        self.__position = position
        self.__rect_size = rect_size
        self.__name = name
        self.__life = 100

    def take_damage(self, value: float) -> None:
        self.__life -= value

        if self.__life <= 0:
            self.queue_free()

    def on_body_collision(self, body, pos_y) -> None:
        pass

    def get_rect_size(self) -> Vector2:
        return self.__rect_size

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

    def get_name(self) -> str:
        return self.__name

    def queue_free(self) -> None:
        if self.__children_manager.get_parent() is not None:
            self.__children_manager.get_parent().remove_child(self)

        self.__collision_body.stop_collision()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.text(50, 40, str(int(self.__life)), 8)
        pyxel.blt(self.get_position().x,
                  self.get_position().y, 2, 0, 0, 32, 96, pyxel.COLOR_PURPLE)
