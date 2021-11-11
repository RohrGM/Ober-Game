from typing import Type

from Interfaces.INode2D import INode2D


class ChildrenManager:
    def __init__(self, agent) -> None:
        self.__agent = agent
        self.__children = []
        self.__parent = None

    def add_child(self, child: Type[INode2D]) -> None:
        self.__children.append(child)
        child.add_parent(self.__agent)

    def remove_child(self, child: Type[INode2D]) -> None:
        self.__children.remove(child)
        child.remove_parent(self.__agent)

    def set_children(self, children: list) -> None:
        for node in self.__children:
            node.remove_parent()

        for node in children:
            node.add_child(self.__agent)

    def get_parent(self) -> Type[INode2D]:
        return self.__parent

    def add_parent(self, parent: Type[INode2D]) -> None:
        self.__parent = parent

    def remove_parent(self) -> None:
        self.__parent = None
