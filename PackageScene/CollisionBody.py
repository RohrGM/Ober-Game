import pyxel

from util import Vector2, CollisionSystem
from interfaces import IOnPyxel, ICollisionEvents


class CollisionBody(ICollisionEvents, IOnPyxel):

    def __init__(self, agent: object, layer: int, mask: int, rect_size: Vector2, reference_pos: Vector2, name: str):
        self.__name = name
        self.__mask = mask
        self.__layer = layer
        self.__rect_size = rect_size
        self.__reference_pos = reference_pos
        self.__agent = agent
        self.__events = {"collision_body": []}

        CollisionSystem.add_body_on_system(self)

    def get_name(self) -> str:
        return self.__name

    def get_layer(self) -> int:
        return self.__layer

    def get_mask(self) -> int:
        return self.__mask

    def get_position(self) -> Vector2:
        return self.__reference_pos

    def get_rect_size(self) -> Vector2:
        return self.__rect_size

    def get_agent(self) -> object:
        return self.__agent

    def check_collisions(self):
        for body in CollisionSystem.collision_layer.copy():
            if self.__mask == body.get_layer():
                collision, pos_y = CollisionSystem.has_colliding(self, body)
                if collision:
                    self.on_collision_body_event(body.get_agent(), body.get_name(), pos_y)

    def stop_collision(self):
        CollisionSystem.remove_body_on_system(self)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def on_collision_body_event(self, agent: object, name: str, pos_y: int) -> None:
        for func in self.__events["collision_body"]:
            func(agent, name, pos_y)

    def update(self) -> None:
        self.check_collisions()

    def draw(self) -> None:
        pass
        '''pyxel.rect(self.get_position().x, self.__reference_pos.y, self.__rect_size.x, self.__rect_size.y, 6)'''
