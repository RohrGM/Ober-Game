import pyxel

from Nodes.BasicNodes.AnimatedSprite import AnimatedSprite
from Nodes.SpecificNodes.Enemy import Enemy
from Scenes.Barricade import Barricade
from Util.Animation import Animation
from Util.Vector2 import Vector2
from random import randrange


class ZombieScene(Enemy):
    def __init__(self, barricade):
        sp = randrange(1, 3)

        super().__init__(position=Vector2(randrange(270, 350), randrange(50, 110)), speed=0.25 if sp == 1 else 1, size=Vector2(14, 28), barricade=barricade, critical_area= 10)

        self.__body = AnimatedSprite(position=Vector2(0, 0), start_anim="run", animations={
            "run": Animation(speed=5, position=Vector2(0, 128), frames=4),
            "attack": Animation(speed=5, position=Vector2(128, 128), frames=4)
        })

    def update(self):
        self.check_collision()
        if self.get_barricade().is_alive() and self.get_position().x <= 55:
            self.__body.set_current_anim_name("attack")
            if pyxel.frame_count % 50 == 0:
                self.get_barricade().take_damage(0.5)
        else:
            self.__body.set_current_anim_name("run")
            movement = self.move(self.get_position(), self.get_speed())
            self.set_position(movement)

    def draw(self):
        anim = self.__body.get_current_animation()
        index = anim.get_index()
        v = anim.get_position().y
        u = (anim.get_size().x * index) + anim.get_position().x

        pyxel.blt(self.get_position().x, self.get_position().y, 0, u, v,
                  anim.get_size().x, anim.get_size().y, pyxel.COLOR_PURPLE)
