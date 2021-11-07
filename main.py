import pyxel

from Nodes.BasicNodes.Node2D import Node2D
from Scenes.MenuScene import MenuScene
from Scenes.OberScene import OberScene
from Scenes.SpawScene import SpawScene
from Scenes.ZombieScene import ZombieScene
from Util.Vector2 import Vector2
from Util.YSort import YSort


class app(Node2D):
    def __init__(self):
        super().__init__(position=Vector2(0, 0))
        pyxel.init(256, 144)
        pyxel.image(0).load(0, 0, "Assets/Player/sprite.png")
        pyxel.image(1).load(0, 0, "Assets/background.png")
        self.__scenes = {
            "menu": [MenuScene()],
            "level1": [OberScene(), SpawScene()]
        }

        self.change_scene("menu")
        pyxel.run(self.update, self.draw)

    def change_scene(self, scene_name: str):
        self.set_children(self.__scenes[scene_name])

    def update(self):
        self.set_children(YSort(self.get_children()).get_ySort())
        for node in self.get_children():
            node.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        for node in self.get_children():
            node.draw()


app()
