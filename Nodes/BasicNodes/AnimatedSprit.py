import pyxel

from Nodes.BasicNodes.Node2D import Node2D
from Util.Vector2 import Vector2


class AnimatedSprite(Node2D):

    def __init__(self, position: Vector2, start_anim: str, animations: dict, name: str):
        super().__init__(position=position, name=name)
        self.__current_anim = start_anim
        self.__animations = animations
        self.__anim_free = True
        self.set_current_anim_name(start_anim)

    def get_current_animation(self):
        return self.__animations[self.__current_anim]

    def get_current_anim_name(self):
        return self.__current_anim

    def set_current_anim_name(self, anim: str):
        if self.__animations[anim].is_loop() is not True:
            self.__anim_free = False
            self.__animations[anim].set_start()
        self.__current_anim = anim

    def is_anim_free(self):
        return self.__anim_free

    def set_anim_free(self, free: bool):
        self.__anim_free = free

    def update(self):
        pass

    def draw(self):
        ctrl_u, ctrl_v = self.get_current_animation().get_uv()
        pyxel.blt(self.get_position().x, self.get_position().y, 0, ctrl_u, ctrl_v,
                  self.get_current_animation().get_size().x, self.get_current_animation().get_size().y,
                  pyxel.COLOR_PURPLE)
