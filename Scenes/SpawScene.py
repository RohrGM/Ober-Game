import pyxel
from random import randrange

from Nodes.BasicNodes.Node2D import Node2D
from PackageScene.Enemy import Enemy
from Util.Vector2 import Vector2


class SpawScene(Node2D):
    def __init__(self):
        super().__init__(position=Vector2(0, 0))
        self.i = 0

    def update(self):
        if pyxel.frame_count % randrange(20, 30) == 0 and self.i == 0:
            self.i = 1
            self.get_parent().add_child(Enemy(position=Vector2(randrange(270, 350), randrange(70, 110))))

    def draw(self):
        pass
