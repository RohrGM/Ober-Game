from abc import ABC, abstractmethod

from Nodes.BasicNodes.Body2D import Body2D


class IBullet(ABC, Body2D):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def on_body_collision(self):
        pass
