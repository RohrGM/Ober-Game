import pyxel

from Nodes.BasicNodes.AnimatedSprite import AnimatedSprite
from Nodes.SpecificNodes.Enemy import Enemy
from Util.Animation import Animation
from Util.Vector2 import Vector2
from random import randrange


class ZombieScene(Enemy):
    def __init__(self):
        sp = randrange(1, 3)

        super().__init__(position=Vector2(randrange(270, 350), randrange(50, 110)), speed=0.5 if sp == 1 else 1, size=Vector2(14, 28))

        self.__body = AnimatedSprite(position=Vector2(0, 0), start_anim="run", animations={
            "run": Animation(speed=5, position=Vector2(0, 128), frames=4)
        })

        self.add_child(self.__body)

    def update(self):
        self.check_collision()
        movement = self.move(self.get_position(), self.get_speed())
        self.set_position(movement)

    def draw(self):
        anim = self.__body.get_current_animation()
        index = anim.get_index()
        v = anim.get_position().y
        u = (anim.get_size().x * index) + anim.get_position().x

        pyxel.blt(self.get_position().x, self.get_position().y, 0, u, v,
                  anim.get_size().x, anim.get_size().y, pyxel.COLOR_PURPLE)
