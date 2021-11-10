import pyxel

from Nodes.BasicNodes.AnimatedSprite import AnimatedSprite
from Nodes.SpecificNodes.Enemy import Enemy
from Util.Animation import Animation
from Util.Vector2 import Vector2
from random import randrange


class ZombieScene(Enemy):

    def __init__(self):
        sp = randrange(1, 3)

        super().__init__(position=Vector2(randrange(270, 350), randrange(70, 110)), speed=0.25 if sp == 1 else 1,
                         size=Vector2(14, 28), critical_area=10)

        self.__body = AnimatedSprite(position=Vector2(-14, 0), start_anim="run", name="body", animations={
            "run": Animation(speed=5, position=Vector2(0, 128), frames=4),
            "attack": Animation(speed=5, position=Vector2(128, 128), frames=4),
            "dead": Animation(speed=3, position=Vector2(0, 160), frames=5, loop=False, agent=self,
                              size=Vector2(32, 32)),
        })

        self.add_child(self.__body)

    def dead(self):
        self.__body.set_current_anim_name("dead")

    def set_anim_free(self, free):
        self.__body.set_anim_free(free)
        if self.__body.get_current_anim_name() == "dead":
            self.queue_free()

    def on_body_collision(self, body, pos_y):
        if body.name == "Barricade":
            if pyxel.frame_count % 35 == 0:
                body.take_damage(.5)
            self.__body.set_current_anim_name("attack")

    def update(self):

        if self.__body.is_anim_free():
            if self.__body.get_current_anim_name() == "run":
                movement = self.move(self.get_position(), self.get_speed())
                self.set_position(movement)

            self.__body.set_current_anim_name("run")
            self.check_collision()

    def draw(self):
        for node in self.get_children():
            node.draw()
