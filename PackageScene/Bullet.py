import pyxel

from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from PackageScene.Enemy import Enemy
from Util.Vector2 import Vector2
from Util.CollisionBody import CollisionBody
from Util.ChildrenManager import ChildrenManager
from typing import Type


class Bullet(IBody2D):

    def __init__(self, position: Vector2, rect_size: Vector2, damage: int, name: str, weapon) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__collision_body = CollisionBody(agent=self, layer=0, mask=1, rect_size=rect_size)
        self.__position = position
        self.__rect_size = rect_size
        self.__damage = damage
        self.__weapon = weapon
        self.__valid = True
        self.__name = name

    def on_body_collision(self, body: Enemy, pos_y: int) -> None:
        if body.get_name() == "Enemy" and self.__valid:
            self.__valid = False
            self.queue_free()
            body.take_damage(self.__damage, pos_y)
            if pos_y < body.get_critical_area():
                self.__weapon.add_critical_count()
                body.take_damage(self.__damage * 2, pos_y)

    def get_rect_size(self) -> Vector2:
        return self.__rect_size

    def add_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.add_child(child)

    def remove_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.remove_child(child)

    def add_parent(self, parent: Type[INode2D]) -> None:
        self.__children_manager.add_parent(parent)

    def get_parent(self) -> Type[INode2D]:
        return self.__children_manager.get_parent()

    def remove_parent(self) -> None:
        self.__children_manager.remove_parent()

    def set_children(self, children: list) -> None:
        self.__children_manager.set_children(children)

    def get_position(self) -> Vector2:
        if self.__children_manager.get_parent() is None:
            return self.__position
        return Vector2.sum_vector(self.__children_manager.get_parent().get_position(), self.__position)

    def set_position(self, position: Vector2):
        self.__position = position

    def get_name(self) -> str:
        return self.__name

    def queue_free(self) -> None:
        if self.__children_manager.get_parent() is not None:
            self.__children_manager.get_parent().remove_child(self)

        self.__collision_body.stop_collision()

    def update(self) -> None:
        self.__collision_body.check_collisions()
        self.set_position(Vector2(self.get_position().x + 10, self.get_position().y))

        if self.get_position().x > 256:
            self.queue_free()

    def draw(self) -> None:
        pyxel.rect(self.get_position().x, self.get_position().y, self.get_rect_size().x,
                   self.get_rect_size().y, 10)
