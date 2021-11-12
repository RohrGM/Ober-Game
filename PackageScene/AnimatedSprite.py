import pyxel

from Interfaces.INode2D import INode2D
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2
from Util.Animation import Animation
from typing import Type


class AnimatedSprite(INode2D):

    def __init__(self, position: Vector2, start_anim: str, animations: dict, name: str) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__position = position
        self.__animations = animations
        self.__current_anim = start_anim
        self.__name = name
        self.__anim_free = True

    def get_current_animation(self) -> Animation:
        return self.__animations[self.__current_anim]

    def get_current_anim_name(self) -> str:
        return self.__current_anim

    def set_current_anim_name(self, anim: str) -> None:
        if self.__animations[anim].is_loop() is not True:
            self.__anim_free = False
            self.__animations[anim].set_start()
        self.__current_anim = anim

    def is_anim_free(self) -> bool:
        return self.__anim_free

    def set_anim_free(self, free: bool) -> None:
        self.__anim_free = free

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
        pass

    def draw(self):
        ctrl_u, ctrl_v = self.get_current_animation().get_uv()
        pyxel.blt(self.get_position().x, self.get_position().y, 0, ctrl_u, ctrl_v,
                  self.get_current_animation().get_size().x, self.get_current_animation().get_size().y,
                  pyxel.COLOR_PURPLE)
