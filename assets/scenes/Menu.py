import pyxel
from assets.interfaces import IOnPyxel
from assets.util import Vector2

MAX_DELAY = 6


class Menu(IOnPyxel):

    def __init__(self, agent: object) -> None:
        self.__agent = agent
        self.__option = 0
        self.__delay = MAX_DELAY

    def get_position(self) -> Vector2:
        return Vector2(0, 0)

    def update(self):
        self.__delay -= 1
        if self.__delay < 0:
            if pyxel.btn(pyxel.KEY_UP):
                self.__delay = MAX_DELAY
                self.__option = 1 if self.__option == 0 else self.__option - 1

            elif pyxel.btn(pyxel.KEY_DOWN):
                self.__delay = MAX_DELAY
                self.__option = 0 if self.__option == 1 else self.__option + 1

            elif pyxel.btn(pyxel.KEY_ENTER):
                if self.__option == 0:
                    self.__agent.change_scene("fight")
                elif self.__option == 1:
                    pyxel.quit()

    def draw(self):
        pyxel.rect(85, 45, 90, 70, 0)
        pyxel.text(113, 65, " INICIAR ", 6 if self.__option == 0 else 1)
        pyxel.text(113, 80, "  SAIR ", 6 if self.__option == 1 else 1)
        pyxel.text(109, 95, "Press ENTER", pyxel.frame_count % 16)
