from abc import abstractmethod

from Nodes.BasicNodes.Body2D import Body2D
from Scenes.Barricade import Barricade
from Util.Vector2 import Vector2


class Enemy(Body2D):

    def __init__(self, position: Vector2, speed: int, size: Vector2, barricade: Barricade, critical_area: int):
        super().__init__(position=position, speed=speed, size=size, layer=1, mask=2, name="Enemy")
        self.__barricade = barricade
        self.__critical_area = critical_area
        self.__life = 2

    def get_barricade(self):
        return self.__barricade

    def on_body_collision(self, body, pos_y):
        pass

    def get_critical_area(self):
        return self.__critical_area

    def take_damage(self, value: int):
        self.__life -= value
        if self.__life <= 0:
            self.queue_free()

    @staticmethod
    def move(position: Vector2, speed: int):
        position.x -= speed
        return position

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
