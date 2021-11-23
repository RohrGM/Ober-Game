import pyxel

from assets.util import Vector2
from assets.interfaces import IOnPyxel, IWeaponEvents, IAnimatedSpriteEvents
from assets.packageScene.BulletPiercing import BulletPiercing
from assets.packageScene.BulletNormal import BulletNormal
from typing import Type


class Weapon(IOnPyxel, IWeaponEvents):

    def __init__(self, fire_rate: int, max_ammo: int, shot_pos: Vector2, reference_pos: Vector2,
                 anim: Type[IAnimatedSpriteEvents], name: str) -> None:
        self.__fire_rate = fire_rate
        self.__max_ammo = max_ammo
        self.__shot_pos = shot_pos
        self.__reference_pos = reference_pos
        self.__name = name

        self.__current_fire_rate = 0
        self.__current_ammo = max_ammo
        self.__anim_locked = False
        self.__special_state = False
        self.__critical_count = 0

        self.__bullets = []

        self.__events = {"shoot": [], "reload": [], "special": []}

        anim.add_subscriber(self.anim_locked, "locked_animation")
        anim.add_subscriber(self.anim_finished, "animation_finished")

    def get_name(self) -> str:
        return self.__name

    def shoot(self) -> None:
        if self.__anim_locked is False and self.__current_fire_rate < 0 < self.__current_ammo:
            self.__current_fire_rate = self.__fire_rate
            self.__current_ammo -= 1

            bullet = BulletPiercing(Vector2.sum(self.__reference_pos, self.__shot_pos),
                                    2.5) if self.__special_state else BulletNormal(
                Vector2.sum(self.__reference_pos, self.__shot_pos), 5)

            bullet.add_subscriber(self.remove_bullet, "dead")
            bullet.add_subscriber(self.add_critical_count, "critical")

            self.__bullets.append(bullet)
            self.shoot_event("shoot")

    def remove_bullet(self, bullet) -> None:
        if bullet in self.__bullets:
            self.__bullets.remove(bullet)

    def add_critical_count(self, value: float) -> None:
        if self.__special_state is False:
            self.__critical_count += value
            if self.__critical_count > 50:
                self.__critical_count = 50

    def start_reload(self) -> None:
        self.reload_event("reload")

    def end_reload(self) -> None:
        self.__current_ammo = self.__max_ammo

    def update_fire_rate(self) -> None:
        self.__current_fire_rate -= 1

    def anim_locked(self, state: bool) -> None:
        self.__anim_locked = state

    def anim_finished(self, animation: str) -> None:
        if animation == "arms_reload":
            self.end_reload()
        elif animation == "arms_special":
            self.__special_state = True

    def special_event(self, anim: str) -> None:
        for func in self.__events["special"]:
            func(anim)

    def shoot_event(self, anim: str) -> None:
        for func in self.__events["shoot"]:
            func(anim)

    def reload_event(self, anim: str) -> None:
        for func in self.__events["reload"]:
            func(anim)

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

            elif pyxel.btn(pyxel.KEY_Q):
                self.special_event("special")

        if self.__special_state:
            self.__critical_count -= .4
            if self.__critical_count <= 0:
                self.__critical_count = 0
                self.__special_state = False

    def draw(self) -> None:
        for bullet in self.__bullets.copy():
            bullet.draw()

        pyxel.rect(15, 10, 52, 4, pyxel.frame_count % 16 if self.__critical_count >= 50 or self.__special_state else 7)
        pyxel.rect(16, 11, self.__critical_count, 2, 2)
        pyxel.blt(2, 5, 0, 232, 7, 11, 12, pyxel.COLOR_PURPLE)

        for i in range(self.__max_ammo):
            pyxel.rect(250 - (4 * i), 130, 3, 13, 0 if self.__current_ammo > 0 else pyxel.frame_count % 16)

        for i in range(self.__current_ammo):
            pyxel.blt(250 - (4 * i), 130, 0, 225, 1, 3, 13, pyxel.COLOR_PURPLE)
