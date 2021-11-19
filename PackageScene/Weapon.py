import pyxel

from util import Vector2
from interfaces import IOnPyxel, IWeaponEvents, IAnimatedSpriteEvents
from .Bullet import Bullet
from typing import Type


class Weapon(IOnPyxel, IWeaponEvents):

    def __init__(self, fire_rate: int, max_ammo: int, shot_pos: Vector2, reference_pos: Vector2, anim: Type[IAnimatedSpriteEvents], name: str) -> None:
        self.__fire_rate = fire_rate
        self.__max_ammo = max_ammo
        self.__shot_pos = shot_pos
        self.__reference_pos = reference_pos
        self.__name = name

        self.__current_fire_rate = 0
        self.__current_ammo = max_ammo
        self.__anim_locked = False
        self.critical_count = 0

        self.__bullets = []

        self.__events = {"shoot": [], "reload": []}

        anim.add_subscriber(self.anim_locked, "locked_animation")
        anim.add_subscriber(self.anim_finished, "animation_finished")

    def get_name(self) -> str:
        return self.__name

    def shoot(self) -> None:
        if self.__anim_locked is False and self.__current_fire_rate < 0 < self.__current_ammo:
            self.__current_fire_rate = self.__fire_rate
            self.__current_ammo -= 1

            bullet = Bullet(Vector2.sum(self.__reference_pos, self.__shot_pos), 5)
            bullet.add_subscriber(self.remove_bullet, "dead")
            bullet.add_subscriber(self.add_critical_count, "critical")

            self.__bullets.append(bullet)
            self.shoot_event()

    def remove_bullet(self, bullet) -> None:
        self.__bullets.remove(bullet)

    def add_critical_count(self, value: float) -> None:
        self.critical_count += value

    def start_reload(self) -> None:
        self.reload_event()

    def end_reload(self) -> None:
        self.__current_ammo = self.__max_ammo

    def update_fire_rate(self) -> None:
        self.__current_fire_rate -= 1

    def anim_locked(self, state: bool) -> None:
        self.__anim_locked = state

    def anim_finished(self, animation: str) -> None:
        if animation == "arms_reload":
            self.end_reload()

    def shoot_event(self) -> None:
        for func in self.__events["shoot"]:
            func()

    def reload_event(self) -> None:
        for func in self.__events["reload"]:
            func()

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def update(self) -> None:
        self.update_fire_rate()

        for bullet in self.__bullets.copy():
            bullet.update()

        if self.__anim_locked is False:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.shoot()
            elif pyxel.btn(pyxel.KEY_R) and self.__current_ammo < self.__max_ammo:
                self.start_reload()

    def draw(self) -> None:

        for bullet in self.__bullets.copy():
            bullet.draw()

        for i in range(self.__max_ammo):
            pyxel.rect(250 - (4 * i), 130, 3, 13, 0 if self.__current_ammo > 0 else pyxel.frame_count % 16)

        for i in range(self.__current_ammo):
            pyxel.blt(250 - (4 * i), 130, 0, 225, 1, 3, 13, pyxel.COLOR_PURPLE)
