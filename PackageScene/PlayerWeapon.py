import pyxel

from Interfaces.INode2D import INode2D
from PackageScene.Bullet import Bullet
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2
from typing import Type


class PlayerWeapon(INode2D):

    def __init__(self, position: Vector2, max_ammo: int, fire_rate: int, damage: int) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__position = position
        self.__max_ammo = max_ammo
        self.__ammo = max_ammo
        self.__fire_rate = fire_rate
        self.__fire_rate_time = 0
        self.__critical_count = 0
        self.__damage = damage
        self.__free = True

    def can_reload(self) -> bool:
        if self.__ammo < self.__max_ammo:
            return True
        return False

    def can_shoot(self) -> bool:
        if self.__fire_rate_time <= 0 < self.__ammo:
            return True
        return False

    def add_critical_count(self) -> None:
        if self.__critical_count < 50:
            self.__critical_count += 2

    def get_critical_count(self) -> int:
        return self.__critical_count

    def set_critical_count(self, critical_count: int) -> None:
        self.__critical_count = critical_count

    def shoot(self, position: Vector2, parent) -> bool:
        if self.can_shoot():
            self.__ammo -= 1
            self.__fire_rate_time = self.__fire_rate
            parent.add_child(Bullet(position=position, rect_size=Vector2(5, 1), damage=self.__damage, name="Bullet", weapon=self))
            return True
        return False

    def reload(self) -> None:
        self.__ammo = self.__max_ammo

    def update_fire_rate_time(self) -> None:
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

    def get_children(self) -> list:
        return self.__children_manager.get_children()

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
        self.update_fire_rate_time()

    def draw(self) -> None:
        for i in range(self.__max_ammo):
            pyxel.rect(250 - (4 * i), 130, 3, 13, 0 if self.__ammo > 0 else pyxel.frame_count % 16)

        for i in range(self.__ammo):
            pyxel.blt(250 - (4 * i), 130, 0, 225, 1, 3, 13, pyxel.COLOR_PURPLE)
