import pyxel
from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class Bullet(Body2D):
    def __init__(self, position, speed):
        super().__init__(position=position, speed=speed, size=Vector2(5, 1), layer=0, mask=1, name="Bullet")
        self.__valid = True

    def on_body_collision(self, body, pos_y):
        if body.name == "Enemy" and self.__valid:
            self.__valid = False

            if pos_y < body.get_critical_area():
                body.take_damage(2)
            else:
                body.take_damage(1)
            self.queue_free()

    def update(self):
        self.check_collision()
        self.set_position(Vector2(self.get_position().x + self.get_speed(), self.get_position().y))

        if self.get_position().x > 256:
            self.queue_free()

    def draw(self):
        pyxel.rect(self.get_position().x, self.get_position().y, self.get_size().x,
                   self.get_size().y, pyxel.COLOR_YELLOW)
