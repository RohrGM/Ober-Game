from abc import ABC, abstractmethod

from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class Enemy(Body2D, ABC):

    def __init__(self, position: Vector2, speed: int, size: Vector2, critical_area: int):
        super().__init__(position=position, speed=speed, size=size, layer=1, mask=2, name="Enemy")
        self.__critical_area = critical_area
        self.__life = 2

    def get_critical_area(self):
        return self.__critical_area

    def take_damage(self, value: int):
        self.__life -= value
        if self.__life <= 0:
            self.dead()

    @abstractmethod
    def dead(self):
        pass

    @staticmethod
    def move(position: Vector2, speed: int):
        position.x -= speed
        return position

