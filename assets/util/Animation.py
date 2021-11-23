import pyxel
from assets.util.Vector2 import Vector2


class Animation:
    def __init__(self, speed: int, position: Vector2, frames: int, loop: bool = True, agent=None, size: Vector2 = Vector2(32, 32)) -> None:
        self.__size = size
        self.__speed = speed
        self.__position = position
        self.__frames = frames
        self.__loop = loop
        self.__agent = agent
        self.__frame_start = 0

    def is_loop(self) -> None:
        return self.__loop

    def get_index(self) -> int:
        index = (pyxel.frame_count // self.__speed) % self.__frames
        if self.__loop is not True:
            index = (pyxel.frame_count - self.__frame_start) // self.__speed
            if index >= self.__frames - 1:
                self.__agent.end_no_loop_anim()

        return index

    def get_uv(self) -> int:
        return (self.__size.x * self.get_index()) + self.__position.x, self.__position.y

    def set_start(self) -> None:
        self.__frame_start = pyxel.frame_count

    def get_size(self) -> Vector2:
        return self.__size

    def get_position(self) -> Vector2:
        return self.__position
