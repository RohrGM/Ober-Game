from PackageScene.AnimatedSprite import AnimatedSprite
from PackageScene.HitMark import HitMark
from Util.ChildrenManager import ChildrenManager
from Util.CollisionBody import CollisionBody
from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from Util.Animation import Animation
from Util.Vector2 import Vector2
from random import randrange
from typing import Type
import pyxel


class Enemy(IBody2D):
    sp = randrange(1, 5)

    def __init__(self, position: Vector2 = Vector2(randrange(270, 350), randrange(70, 110)),
                 rect_size: Vector2 = Vector2(14, 28),
                 name: str = "Enemy") -> None:
        self.__children_manager = ChildrenManager(self)
        self.__collision_body = CollisionBody(agent=self, layer=1, mask=2, rect_size=rect_size)
        self.__position = position
        self.__rect_size = rect_size
        self.__name = name
        self.__critical_area = 8
        self.__life = 2

        self.__body = AnimatedSprite(position=Vector2(-14, 0), start_anim="run", animations={
            "run": Animation(speed=5, position=Vector2(0, 128), frames=4),
            "attack": Animation(speed=5, position=Vector2(128, 128), frames=4),
            "dead": Animation(speed=3, position=Vector2(0, 160), frames=5, loop=False, agent=self,
                              size=Vector2(32, 32)),
        })

        self.add_child(self.__body)

    def take_damage(self, value: int, pos_y: int) -> None:
        self.add_child(HitMark(pos_y=pos_y, image="head" if pos_y < self.__critical_area else "body"))
        self.__life -= value
        if self.__life <= 0:
            self.dead()

    def dead(self) -> None:
        self.__body.set_current_anim_name("dead")
        self.__collision_body.stop_collision()

    def set_anim_free(self, free) -> None:
        if self.__body.get_current_anim_name() == "dead":
            self.queue_free()
        self.__body.set_anim_free(free)

    def get_critical_area(self) -> int:
        return self.__critical_area

    def on_body_collision(self, body: Type[IBody2D], pos_y: int) -> None:
        if body.get_name() == "Barricade" and self.__body.is_anim_free():
            if pyxel.frame_count % 35 == 0:
                body.take_damage(.5)

            self.__body.set_current_anim_name("attack")

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

    def update(self) -> None:
        for node in self.__children_manager.get_children():
            node.update()

        if self.__body.is_anim_free():
            if self.__body.get_current_anim_name() == "run":
                movement = self.move(self.get_position(), 1)
                self.set_position(movement)

            self.__body.set_current_anim_name("run")

        self.__collision_body.check_collisions()

    def draw(self) -> None:
        for node in self.__children_manager.get_children():
            node.draw()

    @staticmethod
    def move(position: Vector2, speed: int):
        position.x -= speed
        return position
