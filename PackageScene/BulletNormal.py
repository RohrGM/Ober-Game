import pyxel

from superclass import Bullet
from util import Vector2


class BulletNormal(Bullet):

    def __init__(self, position: Vector2, damage: float):
        super().__init__(position, damage)

    def on_collision_body(self, agent: object, name: str, pos_y: int) -> None:
        if name == "Enemy" and self.is_valid():
            self.set_valid(False)
            damage = self.get_damage()
            if pos_y < agent.get_critical_area():
                self.critical_event(damage)
                damage *= 2
            agent.take_damage(damage, pos_y)
            self.dead_event(self)

    def bullet_draw(self) -> None:
        pyxel.rect(self.get_position().x, self.get_position().y, self.get_rect_size().x, self.get_rect_size().y, 10)
