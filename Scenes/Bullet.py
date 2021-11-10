import pyxel
from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class Bullet(Body2D):
    def __init__(self, position, speed, agent):
        super().__init__(position=position, speed=speed, size=Vector2(5, 1), layer=0, mask=1, name="Bullet")
        self.__agent = agent
        self.__valid = True

    def on_body_collision(self, body, pos_y):
        if body.name == "Enemy" and self.__valid:

            if self.__agent.is_sp_active() is not True:
                self.__valid = False
                self.queue_free()

            if pos_y < body.get_critical_area():
                self.__agent.add_special()
                body.take_damage(2)
            else:
                body.take_damage(1)

    def update(self):
        self.check_collision()
        self.set_position(Vector2(self.get_position().x + self.get_speed(), self.get_position().y))

        if self.get_position().x > 256:
            self.queue_free()

    def draw(self):
        pyxel.rect(self.get_position().x, self.get_position().y, self.get_size().x,
                   self.get_size().y, pyxel.frame_count % 16 if self.__agent.is_sp_active() else 10)
