import pyxel
from assets.util import Vector2
from assets.Enums import Direction


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
        if direction == Direction.LEFT:
            position.x -= speed

        elif direction == Direction.RIGHT:
            position.x += speed

        elif direction == Direction.UP:
            position.y -= speed

        elif direction == Direction.DOWN:
            position.y += speed

        return position
