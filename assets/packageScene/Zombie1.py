from assets.superclass import Enemy
from assets.util import Vector2


class Zombie1(Enemy):

    def __init__(self, position: Vector2) -> None:
        super().__init__(position, "zombie_1", 8, Vector2(14, 21))
