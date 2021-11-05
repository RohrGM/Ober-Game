from Nodes.BasicNodes.Node2D import Node2D
from Util.Vector2 import Vector2


class AnimatedSprite(Node2D):

    def __init__(self, position: Vector2, start_anim: str, animations: dict):
        super().__init__(position)
        self.__current_anim = start_anim
        self.__animations = animations
        self.__anim_free = True

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
