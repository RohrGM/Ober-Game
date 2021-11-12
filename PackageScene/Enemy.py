from typing import Type
from random import randrange
import pyxel
from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from Util.Animation import Animation
from Util.ChildrenManager import ChildrenManager
from Util.CollisionBody import CollisionBody
from Util.Vector2 import Vector2
from PackageScene.AnimatedSprite import AnimatedSprite


class Enemy(IBody2D):

    sp = randrange(1, 5)

    def __init__(self, position: Vector2 = Vector2(randrange(270, 350), randrange(70, 110)), rect_size: Vector2 = Vector2(14, 28),
                 name: str = "Enemy"):
        self.__children_manager = ChildrenManager(self)
        self.__collision_body = CollisionBody(agent=self, layer=1, mask=2, rect_size=rect_size)
        self.__position = position
        self.__rect_size = rect_size
        self.__name = name
        self.__life = 2

        self.__body = AnimatedSprite(position=Vector2(-14, 0), start_anim="run", name="body", animations={
            "run": Animation(speed=5, position=Vector2(0, 128), frames=4),
            "attack": Animation(speed=5, position=Vector2(128, 128), frames=4),
            "dead": Animation(speed=3, position=Vector2(0, 160), frames=5, loop=False, agent=self,
                              size=Vector2(32, 32)),
        })

        self.add_child(self.__body)

    def take_damage(self, value: int):
        self.__life -= value
        if self.__life <= 0:
            self.dead()

    def dead(self):
        self.__body.set_current_anim_name("dead")
        self.__collision_body.stop_collision()

    def set_anim_free(self, free):
        self.__body.set_anim_free(free)
        if self.__body.get_current_anim_name() == "dead":
            self.queue_free()

    def on_body_collision(self, body, pos_y):
        if body.get_name() == "Barricade":
            if pyxel.frame_count % 35 == 0:
                body.take_damage(.5)

            self.__body.set_current_anim_name("attack")

    def get_rect_size(self):
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

    def update(self):
        self.__collision_body.check_collisions()

        if self.__body.is_anim_free():
            if self.__body.get_current_anim_name() == "run":
                movement = self.move(self.get_position(), 1)
                self.set_position(movement)

            self.__body.set_current_anim_name("run")

    def draw(self):
        for node in self.__children_manager.get_children():
            node.draw()

    @staticmethod
    def move(position: Vector2, speed: int):
        position.x -= speed
        return position
