import pyxel
from util import Vector2


class BodyMoviment:

    @staticmethod
    def control_moviment(position: Vector2, speed: int):

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
        return motion

    @staticmethod
    def simple_moviment(position: Vector2, direction: str, speed: int):
        if direction == "left":
            position.x -= speed

        elif direction == "right":
            position.x += speed

        elif direction == "up":
            position.y -= speed

        elif direction == "down":
            position.y += speed

        return position
