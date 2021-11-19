import pyxel

from util import Vector2, BodyMoviment
from .CollisionBody import CollisionBody
from Enums import Direction
from interfaces import IOnPyxel, IBulletEvents


class Bullet(IOnPyxel, IBulletEvents):

    def __init__(self, position: Vector2, damage: float) -> None:
        self.__position = position
        self.__damage = damage
        self.__rect_size = Vector2(5, 1)
        self.__elements = []
        self.__valid = True
        self.__collision_body = CollisionBody(self, 2, 1, self.__rect_size, self.__position, "Bullet")

        self.__events = {"critical": [], "dead": []}

        self.__collision_body.add_subscriber(self.on_collision_body, "collision_body")

        self.__elements.append(self.__collision_body)

    def is_alive(self) -> bool:
        return self.__alive

    def on_collision_body(self, agent: object, name: str,  pos_y: int) -> None:
        if name == "Enemy" and self.__valid:
            self.__valid = False
            damage = self.__damage
            if pos_y < agent.get_critical_area():
                self.critical_event(damage)
                damage *= 2
            agent.take_damage(damage)
            self.dead_event(self)

    def critical_event(self, damage: float) -> None:
        for func in self.__events["critical"]:
            func(damage)

    def dead_event(self, bullet: object) -> None:
        for func in self.__events["dead"]:
            func(bullet)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def update(self) -> None:
        self.__collision_body.update()
        BodyMoviment.simple_moviment(self.__position, Direction.RIGHT, 15)
        if self.__position.x > 260:
            self.__alive = False

        for e in self.__elements:
            e.update()

    def draw(self) -> None:
        for e in self.__elements:
            e.draw()

        pyxel.rect(self.__position.x, self.__position.y, self.__rect_size.x, self.__rect_size.y, 10)
