from Util.Vector2 import Vector2
from Util.CollisionSystem import CollisionSystem


class CollisionBody:

    def __init__(self, agent, mask: int, layer: int, rect_size: Vector2):
        self.__agent = agent
        self.__mask = mask
        self.__layer = layer
        self.__rect_size = rect_size
        CollisionSystem.add_body_on_system(self)

    def get_layer(self) -> int:
        return self.__layer

    def get_mask(self) -> int:
        return self.__mask

    def get_position(self) -> Vector2:
        return self.__agent.get_position()

    def get_rect_size(self):
        return self.__rect_size

    def get_agent(self):
        return self.__agent

    def check_collisions(self):
        for body in CollisionSystem.collision_layer.copy():
            if self.__mask == body.get_layer():
                test, pos_y = CollisionSystem.has_colliding(self, body)
                if test:
                    self.__agent.on_body_collision(body=body.get_agent(), pos_y=pos_y)

    def stop_collision(self):
        CollisionSystem.remove_body_on_system(self)
