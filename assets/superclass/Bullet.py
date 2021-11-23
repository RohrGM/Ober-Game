from abc import abstractmethod
from assets.packageScene.CollisionBody import CollisionBody
from assets.util import Vector2, BodyMoviment
from assets.Enums import Direction
from assets.interfaces import IOnPyxel, IBulletEvents


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

    @abstractmethod
    def on_collision_body(self, agent: object, name: str, pos_y: int) -> None:
        pass

    @abstractmethod
    def bullet_draw(self) -> None:
        pass

    def is_valid(self) -> bool:
        return self.__valid

    def set_valid(self, valid) -> None:
        self.__valid = valid

    def get_damage(self) -> float:
        return self.__damage

    def get_position(self) -> Vector2:
        return self.__position

    def get_rect_size(self) -> Vector2:
        return self.__rect_size

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
            self.dead_event(self)

        for e in self.__elements:
            e.update()

    def draw(self) -> None:
        for e in self.__elements:
            e.draw()

        self.bullet_draw()

