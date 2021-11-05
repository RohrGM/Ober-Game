import pyxel

from Nodes.BasicNodes.Node2D import Node2D
from Util.Vector2 import Vector2

MAX_DELAY = 6


class MenuScene(Node2D):

    def __init__(self):
        super().__init__(Vector2(0, 0))
        self.__option = 0
        self.__delay = 0

    def draw(self):
        pyxel.rect(85, 45, 90, 70, 0)
        pyxel.text(113, 72, "CONTINUAR", 6 if self.__option == 0 else 1)
        pyxel.text(113, 80, " INICIAR ", 6 if self.__option == 1 else 1)
        pyxel.text(113, 88, "  SAIR ", 6 if self.__option == 2 else 1)

    def update(self):
        self.__delay -= 1
        if pyxel.btn(pyxel.KEY_UP) and self.__delay < 0:
            self.__delay = MAX_DELAY
            self.__option = 2 if self.__option == 0 else self.__option - 1

        elif pyxel.btn(pyxel.KEY_DOWN) and self.__delay < 0:
            self.__delay = MAX_DELAY
            self.__option = 0 if self.__option == 2 else self.__option + 1

        elif pyxel.btn(pyxel.KEY_ENTER):
            self.get_parent().change_scene("level1")
