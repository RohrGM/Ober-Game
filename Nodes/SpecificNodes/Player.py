from abc import ABC

import pyxel
from Nodes.BasicNodes.Body2D import Body2D
from Scenes.Bullet import Bullet
from Util.Vector2 import Vector2


class Player(Body2D, ABC):
    def __init__(self, position: Vector2, speed: int):
        super().__init__(position=position, speed=speed, size=Vector2(14, 28), name="Player")
        self.__ammo = 7
        self.__fire_rate = 20
        self.__can_shoot = 0
        self.__special = .0
        self.__sp_active = False

    def shoot(self, position: Vector2):
        self.__ammo -= 1
        self.get_parent().add_child(Bullet(position, 10, self))
        self.__can_shoot = self.__fire_rate

    def update_fire_rate(self):
        if self.__can_shoot > 0:
            self.__can_shoot -= 1

    def can_shoot(self):
        if self.__can_shoot == 0:
            if self.__ammo > 0:
                return True
        return False

    def on_body_collision(self, body, pos_y):
        pass

    def reload(self):
        self.__ammo = 7

    def get_ammo(self):
        return self.__ammo

    def add_special(self):
        if self.__special < 50 and self.__sp_active is False:
            self.__special += 2

    def time_sp(self):
        if self.__sp_active:
            self.__special -= 0.25
            if self.__special <= 0:
                self.__special = 0
                self.__sp_active = False

    def is_sp_active(self):
        return self.__sp_active

    def get_special(self):
        return int(self.__special)

    def active_special(self):
        self.__sp_active = True


    @staticmethod
    def move(position: Vector2, speed: int):
        motion = 0
        if pyxel.btn(pyxel.KEY_W):
            position.y -= speed
            motion = 1

        if pyxel.btn(pyxel.KEY_S):
            position.y += speed
            motion = 1

        if pyxel.btn(pyxel.KEY_D):
            position.x += speed
            motion = 1

        if pyxel.btn(pyxel.KEY_A):
            position.x -= speed
            motion = -1

        position.y = max(position.y, 50)
        position.y = min(position.y, 110)
        position.x = max(position.x, 0)
        position.x = min(position.x, 25)
        return position, motion

    @staticmethod
    def update_anim(motion):
        if motion == 0:
            return "idle"
        else:
            return "run"
