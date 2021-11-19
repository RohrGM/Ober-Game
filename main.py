import pyxel

from scenes import Player, EnemySpawn
from util import Vector2


class App:
    def __init__(self):
        pyxel.init(256, 144)
        pyxel.image(0).load(0, 0, "assets/player/sprite.png")
        pyxel.image(1).load(0, 0, "assets/background.png")
        pyxel.image(2).load(0, 0, "assets/static_items.png")

        self.__player = Player(Vector2(20, 50))
        self.__enemy_spawn = EnemySpawn()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.__player.update()
        self.__enemy_spawn.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        self.__player.draw()
        self.__enemy_spawn.draw()


App()

