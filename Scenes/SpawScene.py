import pyxel
from random import randrange

from Nodes.BasicNodes.Node2D import Node2D
from Scenes.ZombieScene import ZombieScene
from Util.Vector2 import Vector2


class SpawScene(Node2D):
    def __init__(self, barricade):
        super().__init__(position=Vector2(0, 0))
        self.__barricade = barricade

    def update(self):
        if pyxel.frame_count % randrange(20, 30) == 0:
            self.get_parent().add_child(ZombieScene(self.__barricade))

    def draw(self):
        pass
