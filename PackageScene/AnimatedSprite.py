import pyxel

from interfaces import IAnimatedSpriteEvents, ISubscriber, IOnPyxel
from util import Vector2, AnimationData


class AnimatedSprite(IAnimatedSpriteEvents, ISubscriber, IOnPyxel):

    def __init__(self, position: Vector2, start_anim: str, character: str, list_name: list,
                 reference_pos: Vector2 = Vector2(0, 0)) -> None:
        self.__position = position
        self.__reference_pos = reference_pos
        self.__animations = AnimationData.get_anim_list(character, list_name, self)
        self.__current_anim = ""
        self.__events = {"animation_finish": [], "locked_animation": []}
        self.set_current_anim(start_anim)

    def set_current_anim(self, anim_name: str) -> None:
        if self.is_anim_valid(anim_name):
            if self.__animations[anim_name].is_loop() is not True:
                self.locked_animation_event(True)
                self.__animations[anim_name].set_start()
            self.__current_anim = anim_name

    def is_anim_valid(self, anim: str) -> bool:
        if anim in self.__animations.keys():
            return True
        return False

    def end_no_loop_anim(self) -> None:
        self.locked_animation_event(False)

    def get_position(self):
        return Vector2.sum_vector(self.__position, self.__reference_pos)

    def animation_finish_event(self, animation_name: str) -> None:
        for func in self.__events["animation_finish"]:
            func()

    def locked_animation_event(self, state: bool) -> None:
        for func in self.__events["locked_animation"]:
            func(state)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        ctrl_u, ctrl_v = self.__animations[self.__current_anim].get_uv()
        pyxel.blt(self.get_position().x,
                  self.get_position().y, 0, ctrl_u, ctrl_v,
                  self.__animations[self.__current_anim].get_size().x,
                  self.__animations[self.__current_anim].get_size().y,
                  pyxel.COLOR_PURPLE)

