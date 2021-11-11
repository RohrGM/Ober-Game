from abc import abstractmethod

from Util.Vector2 import Vector2


class Node2D:

    def __init__(self, position: Vector2, name: str = None):
        self.__position = position
        self.__children = []
        self.__parent = None
        self.name = name

    def add_child(self, child):
        self.__children.append(child)
        child.add_parent(self)

    def add_parent(self, parent):
        self.__parent = parent

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def set_children(self, children: list):
        for node in children:
            if node.get_parent() != self:
                node.add_parent(self)
        self.__children = children

    def remove_child(self, child):
        self.__children.remove(child)

    def get_position(self):
        if self.__parent is not None:
            return Vector2.sum_vector(self.__position, self.__parent.get_position())
        return self.__position

    def set_position(self, position: Vector2):
        self.__position = position

    def queue_free(self):
        if self.get_parent() is not None:
            if self in self.get_parent().get_children():
                self.get_parent().remove_child()
