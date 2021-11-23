import pyxel
from assets.interfaces import IOnPyxel
from assets.packageScene import CollisionBody
from assets.util import Vector2


class Barricade(IOnPyxel):

    def __init__(self, agent: object) -> None:
        self.__life = 100
        self.__position = Vector2(40, 50)
        self.__rect_size = Vector2(32, 96)
        self.__agent = agent
        self.__elements = []
        self.__events = {"dead": []}

        self.__collision_body = CollisionBody(self, 0, 0, self.__rect_size, self.__position, "Barricade")

        self.__elements.append(self.__collision_body)

    def take_damage(self, value: float) -> None:
        self.__life -= value
        if self.__life < 0:
            self.dead()

    def get_position(self) -> Vector2:
        return self.__position

    def dead(self) -> None:
        self.__agent.change_scene("gameover")

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.text(50, 40, str(int(self.__life)), 8)
        pyxel.blt(self.__position.x,
                  self.__position.y, 2, 0, 0, 32, 96, pyxel.COLOR_PURPLE)
