import pyxel
from util import Vector2
from interfaces import IOnPyxel
from superclass import Enemy
from random import randint


class EnemySpawn(IOnPyxel):

    def __init__(self):
        self.__elements = []

    def enemy_dead(self, enemy: Enemy) -> None:
        self.__elements.remove(enemy)

    def spawn(self) -> None:
        enemy = Enemy(Vector2(randint(270, 350), randint(70, 110)), 10)
        enemy.add_subscriber(self.enemy_dead, "dead")
        self.__elements.append(enemy)

    def update(self) -> None:
        if pyxel.frame_count % 30 == 0:
            self.spawn()

        for e in self.__elements.copy():
            e.update()

    def draw(self) -> None:
        for e in self.__elements.copy():
            e.draw()
