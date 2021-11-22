import pyxel
from interfaces import IOnPyxel, IBarricadeEvents
from packageScene import CollisionBody
from util import Vector2


class Barricade(IOnPyxel, IBarricadeEvents):

    def __init__(self):
        self.__life = 100
        self.__position = Vector2(40, 50)
        self.__rect_size = Vector2(32, 96)
        self.__elements = []
        self.__events = {"dead": []}

        self.__collision_body = CollisionBody(self, 0, 0, self.__rect_size, self.__position, "Barricade")

        self.__elements.append(self.__collision_body)

    def take_damage(self, value: float) -> None:
        self.__life -= value
        self.dead_event(self)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def dead_event(self, agent: object):
        for func in self.__events["dead"]:
            func(agent)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.text(50, 40, str(int(self.__life)), 8)
        pyxel.blt(self.__position.x,
                  self.__position.y, 2, 0, 0, 32, 96, pyxel.COLOR_PURPLE)
