import pyxel

from Nodes.BasicNodes.Node2D import Node2D
from Util.Vector2 import Vector2


class Barricade(Node2D):

    def __init__(self):
        super().__init__(Vector2(40, 50), "Barricade")
        self.__alive = True
        self.__life = 100.0

    def take_damage(self, value: float):
        self.__life -= value

        if self.__life <= 0:
            self.__alive = False

    def is_alive(self):
        return self.__alive

    def update(self):
        pass

    def draw(self):
        if self.__alive:
            pyxel.text(50, 40, str(int(self.__life)), 8)
            pyxel.blt(self.get_position().x, self.get_position().y, 2, 0, 0, 64, 96, pyxel.COLOR_PURPLE)
