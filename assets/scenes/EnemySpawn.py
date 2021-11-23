import pyxel
from assets.util import Vector2
from assets.interfaces import IOnPyxel
from assets.packageScene import Zombie0, Zombie1
from assets.superclass import Enemy
from random import randint


class EnemySpawn(IOnPyxel):

    def __init__(self, agent: object) -> None:
        self.__agent = agent

    def get_position(self) -> Vector2:
        return Vector2(0, 0)

    def enemy_dead(self, enemy: Enemy) -> None:
        self.__agent.remove_element(enemy)

    def spawn(self) -> None:
        rand = randint(1, 2)
        enemy = Zombie0(Vector2(randint(270, 350), randint(70, 110))) if rand == 1 else Zombie1(Vector2(randint(270, 350), randint(70, 110)))
        enemy.add_subscriber(self.enemy_dead, "dead")
        self.__agent.add_element(enemy)

    def update(self) -> None:

        if pyxel.frame_count % 30 == 0:
            self.spawn()

    def draw(self) -> None:
        pass
