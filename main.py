import pyxel
from assets.util import Vector2, YSort, CollisionSystem
from assets.scenes import Player, EnemySpawn, Barricade, Menu, GameOver


class App:
    def __init__(self):
        pyxel.init(256, 144)
        pyxel.image(0).load(0, 0, "assets/player/sprite.png")
        pyxel.image(1).load(0, 0, "assets/background.png")
        pyxel.image(2).load(0, 0, "assets/static_items.png")

        self.__elements = []

        self.__scenes = {
            "menu": self.menu_scene,
            "fight": self.fight_scene,
            "gameover": self.gameover_scene
        }
        self.change_scene("menu")

        pyxel.run(self.update, self.draw)

    def menu_scene(self) -> list:
        return [Menu(self)]

    def fight_scene(self) -> list:
        return [Player(Vector2(20, 50)), EnemySpawn(self), Barricade(self)]

    def gameover_scene(self) -> list:
        return [GameOver(self)]

    def change_scene(self, scene_name) -> None:
        CollisionSystem.reset()
        try:
            self.__elements = self.__scenes[scene_name]()
        except() as e:
            print("Nenhum cena com esse nome ", e)

    def add_element(self, element: object) -> None:
        self.__elements.append(element)

    def remove_element(self, agent: object) -> None:
        if agent in self.__elements:
            self.__elements.remove(agent)

    def update(self) -> None:
        for e in self.__elements.copy():
            e.update()

        YSort.get_YSort(self.__elements)

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        for e in self.__elements.copy():
            e.draw()


App()
