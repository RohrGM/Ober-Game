from util import Vector2, BodyMoviment
from interfaces import IOnPyxel, ISubscriber
from packageScene import AnimatedSprite, Weapon


class Enemy:

    def __init__(self, position: Vector2):
        self.__position = position

        self.__life = 10



