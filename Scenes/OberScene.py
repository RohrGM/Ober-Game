import pyxel

from Nodes.BasicNodes.AnimatedSprite import AnimatedSprite
from Nodes.SpecificNodes.Player import Player
from Util.Animation import Animation
from Util.Vector2 import Vector2


class OberScene(Player):
    def __init__(self):
        super().__init__(position=Vector2(10, 75), speed=1)
        self.__arms = AnimatedSprite(position=Vector2(0, 0), start_anim="idle", animations={
            "idle": Animation(speed=7, position=Vector2(0, 0), frames=3),
            "run": Animation(speed=5, position=Vector2(96, 0), frames=4),
            "shoot": Animation(speed=2, position=Vector2(0, 32), frames=3, loop=False, agent=self),
            "reload": Animation(speed=4, position=Vector2(0, 96), frames=8, loop=False, agent=self)
        })
        self.__legs = AnimatedSprite(position=Vector2(0, 0), start_anim="idle", animations={
            "idle": Animation(speed=7, position=Vector2(0, 64), frames=3),
            "run": Animation(speed=5, position=Vector2(96, 64), frames=4)
        })

        self.add_child(self.__arms)
        self.add_child(self.__legs)

    def set_anim_free(self, free):
        self.__arms.set_anim_free(free)
        self.__legs.set_anim_free(free)

        if self.__arms.get_current_anim_name() == "reload":
            self.reload()

    def update(self):
        self.check_collision()
        movement, motion = self.move(self.get_position(), self.get_speed())
        self.update_fire_rate()

        if pyxel.btn(pyxel.KEY_SPACE) and self.can_shoot() and self.__arms.is_anim_free():
            self.shoot(Vector2(self.get_position().x + 24, self.get_position().y + 14))
            self.__arms.set_current_anim_name("shoot")

        elif pyxel.btn(pyxel.KEY_R) and self.__arms.is_anim_free() and self.get_ammo() < 7:
            self.__arms.set_current_anim_name("reload")

        self.set_position(movement)
        self.__legs.set_current_anim_name(self.update_anim(motion))

        if self.__arms.is_anim_free():
            self.__arms.set_current_anim_name(self.update_anim(motion))

    def draw(self):

        for i in range(self.get_ammo()):
            pyxel.blt(245 - (7 * i), 121, 0, 224, 0, 32, 32, pyxel.COLOR_PURPLE)

        arms_anim = self.__arms.get_current_animation()
        legs_anim = self.__legs.get_current_animation()

        ctrl_u, ctrl_v = arms_anim.get_uv()
        legs_u, legs_v = legs_anim.get_uv()

        pyxel.blt(self.__arms.get_position().x, self.__arms.get_position().y, 0, ctrl_u, ctrl_v,
                  arms_anim.get_size().x, arms_anim.get_size().y, pyxel.COLOR_PURPLE)

        pyxel.blt(self.__legs.get_position().x, self.__legs.get_position().y, 0, legs_u, legs_v,
                  legs_anim.get_size().x, legs_anim.get_size().y, pyxel.COLOR_PURPLE)
