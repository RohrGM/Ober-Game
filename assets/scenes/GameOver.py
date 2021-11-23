import pyxel
from assets.interfaces import IOnPyxel
from assets.util import Vector2


class GameOver(IOnPyxel):

    def __init__(self, agent: object) -> None:
        self.__agent = agent

    def get_position(self) -> Vector2:
        return Vector2(0, 0)

    def update(self):
        if pyxel.btn(pyxel.KEY_ENTER):
            self.__agent.change_scene("menu")

    def draw(self):
        pyxel.rect(85, 45, 90, 70, 0)
        pyxel.text(109, 70, " GAME OVER ", 6)
        pyxel.text(109, 90, "Press ENTER", pyxel.frame_count % 16)

