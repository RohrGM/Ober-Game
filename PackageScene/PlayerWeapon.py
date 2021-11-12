import pyxel

from Interfaces.INode2D import INode2D
from PackageScene.Bullet import Bullet
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2
from typing import Type


class PlayerWeapon(INode2D):

    def __init__(self, position: Vector2, max_ammo: int, fire_rate: int, name: str) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__position = position
        self.__max_ammo = max_ammo
        self.__ammo = max_ammo
        self.__fire_rate = fire_rate
        self.__fire_rate_time = 0
        self.__name = name
        self.__free = True

    def can_reload(self) -> bool:
        if self.__ammo < self.__max_ammo:
            return True
        return False

    def can_shoot(self) -> bool:
        if self.__fire_rate_time <= 0 < self.__ammo:
            return True
        return False

    def shoot(self, position: Vector2, parent) -> None:
        if self.can_shoot():
            self.__ammo -= 1
            self.__fire_rate_time = self.__fire_rate
            parent.add_child(Bullet(position=position, rect_size=Vector2(5, 1), name="Bullet", agent=self))

    def reload(self) -> None:
        self.__ammo = self.__max_ammo

    def update_fire_rate_time(self):
        self.__fire_rate_time -= 1

    def set_free(self, free) -> None:
        self.__free = free

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

    def update(self):
        self.update_fire_rate_time()

    def draw(self):
        for i in range(self.__ammo):
            pyxel.blt(245 - (7 * i), 128, 0, 224, 6, 7, 13, pyxel.COLOR_PURPLE)