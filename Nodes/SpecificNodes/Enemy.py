from abc import abstractmethod

from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class Enemy(Body2D):

    def __init__(self, position: Vector2, speed: int, size: Vector2):
        super().__init__(position=position, speed=speed, size=size, layer=1, mask=2, name="Enemy")

    def on_body_collision(self, body):
        pass

    def hit(self):
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
