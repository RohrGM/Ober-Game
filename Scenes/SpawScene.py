import pyxel
from random import randrange

from Nodes.BasicNodes.Node2D import Node2D
from Scenes.ZombieScene import ZombieScene
from Util.Vector2 import Vector2


class SpawScene(Node2D):
    def __init__(self):
        super().__init__(position=Vector2(0, 0))

    def update(self):
        if pyxel.frame_count % randrange(20, 30) == 0:
            self.get_parent().add_child(ZombieScene())

    def draw(self):
        pass
