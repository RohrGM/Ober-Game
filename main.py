import pyxel

from scenes import Player, EnemySpawn
from packageScene import Barricade
from util import Vector2


class App:
    def __init__(self):
        pyxel.init(256, 144)
        pyxel.image(0).load(0, 0, "assets/player/sprite.png")
        pyxel.image(1).load(0, 0, "assets/background.png")
        pyxel.image(2).load(0, 0, "assets/static_items.png")

        self.__elements = []

        self.__player = Player(Vector2(20, 50))
        self.__enemy_spawn = EnemySpawn()
        self.__barricade = Barricade()

        self.__barricade.add_subscriber(self.remove_element, "dead")

        self.__elements.append(self.__player)
        self.__elements.append(self.__enemy_spawn)
        self.__elements.append(self.__barricade)
        pyxel.run(self.update, self.draw)

    def remove_element(self, agent: object):
        if agent in self.__elements:
            self.__elements.remove(agent)

    def update(self):
        for e in self.__elements:
            e.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        for e in self.__elements:
            e.draw()


App()

