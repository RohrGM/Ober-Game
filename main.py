import pyxel

from Nodes.BasicNodes.Node2D import Node2D
from Scenes.MenuScene import MenuScene
from Scenes.OberScene import OberScene
from Scenes.SpawScene import SpawScene
from Scenes.ZombieScene import ZombieScene
from Util.Vector2 import Vector2


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
        for node in self.get_children():
            node.update()

        '''for enemy in self.__enemies.copy():
            for bullet in self.__bullets.copy():
                if enemy.has_colliding(bullet):
                    enemy.set_alive(False)
                    bullet.set_alive(False)
                    if enemy in self.__enemies:
                        self.__enemies.remove(enemy)

                    if bullet in self.__bullets:
                        self.__bullets.remove(bullet)'''

    def draw(self):
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        for node in self.get_children():
            node.draw()


app()
