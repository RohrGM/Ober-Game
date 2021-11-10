from abc import abstractmethod

from Nodes.BasicNodes.Node2D import Node2D
from Util.Vector2 import Vector2


class Body2D(Node2D):
    collision_layer = []
    collision_mask = []

    def __init__(self, position: Vector2, speed: float, size: Vector2, layer: int = None, mask: int = None, name: str = None):
        super().__init__(position, name)
        self.__size = size
        self.__motion = 1
        self.__speed = speed
        self.__layer = layer
        self.__mask = mask
        Body2D.collision_layer.append(self)
        Body2D.collision_mask.append(self)

    def check_collision(self):
        for body in Body2D.collision_layer.copy():
            if self.__mask == body.get_layer():
                test, pos_y = self.has_colliding(body)
                if test:
                    self.on_body_collision(body=body, pos_y=pos_y)

    @abstractmethod
    def on_body_collision(self, body, pos_y):
        pass

    def queue_free(self):
        if self.get_parent() is not None:
            if self in self.get_parent().get_children():
                Body2D.collision_layer.remove(self)
                Body2D.collision_mask.remove(self)
                self.get_parent().remove_child(self)

    def get_speed(self):
        return self.__speed

    def get_motion(self):
        return self.__motion

    def get_size(self):
        return self.__size

    def get_layer(self):
        return self.__layer

    def has_colliding(self, other_body2D):
        if self != other_body2D and self.get_position().x + self.get_size().x > other_body2D.get_position().x \
                and other_body2D.get_position().x + other_body2D.get_size().x > self.get_position().x \
                and self.get_position().y + self.get_size().y > other_body2D.get_position().y \
                and other_body2D.get_position().y + other_body2D.get_size().y > self.get_position().y:
            return True, self.get_position().y - other_body2D.get_position().y
        return False, 0
