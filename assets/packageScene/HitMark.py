import pyxel

from assets.interfaces import IOnPyxel, IHitMarkEvents
from assets.util import Vector2


class HitMark(IOnPyxel, IHitMarkEvents):

    def __init__(self, head: bool, pos_y: int, reference_pos: Vector2) -> None:
        self.__position = reference_pos
        self.__head = head
        self.__pos_y = pos_y
        self.__events = {"dead": []}
        self.__life = 5

    def dead_event(self, agent: object) -> None:
        for func in self.__events["dead"]:
            func(agent)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def update(self) -> None:
        self.__life -= 1
        if self.__life < 0:
            self.dead_event(self)

    def draw(self) -> None:
        pyxel.blt(self.__position.x + 3, self.__position.y + self.__pos_y - 3, 0, 232 if self.__head else 225, 25, 5, 6,
                  pyxel.COLOR_PURPLE)
