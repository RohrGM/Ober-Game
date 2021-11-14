from typing import Type

import pyxel

from Interfaces.INode2D import INode2D
from PackageScene.Barricade import Barricade
from PackageScene.SpawEnemy import SpawEnemy
from Scenes.MenuScene import MenuScene
from PackageScene.Player import Player
from Util.ChildrenManager import ChildrenManager
from Util.Vector2 import Vector2
from Util.YSort import YSort


class MainScene(INode2D):

    def __init__(self, position: Vector2 = Vector2(0, 0)) -> None:
        self.__children_manager = ChildrenManager(self)
        self.__position = position

        pyxel.init(256, 144)
        pyxel.image(0).load(0, 0, "../Assets/Player/sprite.png")
        pyxel.image(1).load(0, 0, "../Assets/background.png")
        pyxel.image(2).load(0, 0, "../Assets/static_items.png")
        self.__scenes = {
            "Menu": [MenuScene()],
            "Level1": [Player(), SpawEnemy(), Barricade()]
        }

    def start(self) -> None:
        self.change_scene("Menu")
        pyxel.run(self.update, self.draw)

    def change_scene(self, scene_name: str) -> None:
        self.set_children(self.__scenes[scene_name])

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

    def get_children(self) -> list:
        return self.__children_manager.get_children()

    def get_position(self) -> Vector2:
        if self.__children_manager.get_parent() is None:
            return self.__position
        return Vector2.sum_vector(self.__children_manager.get_parent().get_position(), self.__position)

    def set_position(self, position: Vector2) -> None:
        self.__position = position

    def queue_free(self) -> None:
        if self.get_parent() is not None:
            self.get_parent().remove_child(self)

    def update(self) -> None:
        self.set_children(YSort().get_ySort(self.get_children().copy()))
        for node in self.get_children().copy():
            node.update()

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_CYAN)
        pyxel.blt(0, 0, 1, 0, 0, 256, 144)
        for node in self.get_children().copy():
            node.draw()
