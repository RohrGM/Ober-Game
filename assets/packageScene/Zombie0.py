from assets.superclass import Enemy
from assets.util import Vector2


class Zombie0(Enemy):

    def __init__(self, position: Vector2) -> None:
        super().__init__(position, "zombie_0", 8, Vector2(14, 28))
