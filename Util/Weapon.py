import pyxel

from PackageScene.Bullet import Bullet
from Util.Vector2 import Vector2


class Weapon:

    def __init__(self, max_ammo: int, fire_rate: int) -> None:
        self.__max_ammo = max_ammo
        self.__ammo = max_ammo
        self.__fire_rate = fire_rate
        self.__fire_rate_time = 0

    def can_reload(self) -> bool:
        if self.__ammo < self.__max_ammo:
            return True
        return False

    def can_shoot(self) -> bool:
        if self.__fire_rate_time <= 0 < self.__ammo:
            return True
        return False

    def shoot(self, position: Vector2, parent) -> bool:
        if self.can_shoot():
            self.__ammo -= 1
            self.__fire_rate_time = self.__fire_rate
            parent.add_child(Bullet(position=position, rect_size=Vector2(5, 1), name="Bullet", agent=self))
            return True
        return False

    def reload(self) -> None:
        self.__ammo = self.__max_ammo

    def update_fire_rate_time(self):
        self.__fire_rate_time -= 1

    def draw_ammo(self):
        for i in range(self.__ammo):
            pyxel.blt(245 - (7 * i), 128, 0, 224, 6, 7, 13, pyxel.COLOR_PURPLE)

