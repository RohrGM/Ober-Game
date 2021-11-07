from abc import abstractmethod

import pyxel
from Nodes.BasicNodes.Body2D import Body2D
from Nodes.SpecificNodes.Bullet import Bullet
from Util.Vector2 import Vector2


class Player(Body2D):
    def __init__(self, position: Vector2, speed: int):
        super().__init__(position=position, speed=speed, size=Vector2(14, 28), name="Player")
        self.__ammo = 7
        self.__fire_rate = 20
        self.__can_shoot = 0

    def shoot(self, position: Vector2):
        self.__ammo -= 1
        bullet = Bullet(position, 10)
        self.get_parent().add_child(bullet)
        self.__can_shoot = self.__fire_rate

    def update_fire_rate(self):
        if self.__can_shoot > 0:
            self.__can_shoot -= 1

    def can_shoot(self):
        if self.__can_shoot == 0:
            if self.__ammo > 0:
                return True
        return False

    def on_body_collision(self, body):
        pass

    def reload(self):
        self.__ammo = 7

    def get_ammo(self):
        return self.__ammo

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

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
