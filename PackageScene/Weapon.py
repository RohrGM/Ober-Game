import pyxel

from util import Vector2
from interfaces import IOnPyxel


class Weapon(IOnPyxel):

    def __init__(self, fire_rate: int, max_ammo: int, shot_pos: Vector2, reference_pos: Vector2, name: str) -> None:
        self.__fire_rate = fire_rate
        self.__max_ammo = max_ammo
        self.__shot_pos = shot_pos
        self.__reference_pos = reference_pos
        self.__name = name

        self.__current_fire_rate = 0
        self.__current_ammo = max_ammo

    def get_name(self) -> str:
        return self.__name

    def shoot(self) -> None:
        print("atirando")

    def update_fire_rate(self) -> None:
        self.__fire_rate -= 1

    def update(self) -> None:
        self.update_fire_rate()

    def draw(self) -> None:
        for i in range(self.__max_ammo):
            pyxel.rect(250 - (4 * i), 130, 3, 13, 0 if self.__current_ammo > 0 else pyxel.frame_count % 16)

        for i in range(self.__current_ammo):
            pyxel.blt(250 - (4 * i), 130, 0, 225, 1, 3, 13, pyxel.COLOR_PURPLE)
