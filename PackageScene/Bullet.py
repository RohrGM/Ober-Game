import pyxel

from util import Vector2, BodyMoviment
from interfaces import IOnPyxel


class Bullet(IOnPyxel):

    def __init__(self, position: Vector2):
        self.__position = position
        self.__rect_size = Vector2(5, 1)
        self.__alive = True

    def is_alive(self) -> bool:
        return self.__alive

    def update(self) -> None:
        BodyMoviment.simple_moviment(self.__position, "right", 20)
        if self.__position.x > 260:
            self.__alive = False

    def draw(self) -> None:
        pyxel.rect(self.__position.x, self.__position.y, self.__rect_size.x, self.__rect_size.y, 10)
