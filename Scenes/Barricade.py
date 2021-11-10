import pyxel

from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class Barricade(Body2D):

    def __init__(self):
        super().__init__(position=Vector2(40, 50), speed=0, size=Vector2(32, 96), layer=2, mask=3, name="Barricade")
        self.__life = 100.0

    def on_body_collision(self, body, pos_y):
        pass

    def take_damage(self, value: float):
        self.__life -= value

        if self.__life <= 0:
            self.queue_free()

    def update(self):
        pass

    def draw(self):
        pyxel.text(50, 40, str(int(self.__life)), 8)
        pyxel.blt(self.get_position().x,
                  self.get_position().y, 2, 0, 0, 32, 96, pyxel.COLOR_PURPLE)
