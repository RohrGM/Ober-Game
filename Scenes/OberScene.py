import pyxel

from Nodes.BasicNodes.AnimatedSprite import AnimatedSprite
from Nodes.SpecificNodes.Player import Player
from Util.Animation import Animation
from Util.Vector2 import Vector2


class OberScene(Player):

    def __init__(self):
        super().__init__(position=Vector2(10, 75), speed=1)
        self.__arms = AnimatedSprite(position=Vector2(0, 0), start_anim="idle", name="arms", animations={
            "idle": Animation(speed=7, position=Vector2(0, 0), frames=3, size=Vector2(32, 19)),
            "run": Animation(speed=5, position=Vector2(96, 0), frames=4, size=Vector2(32, 19)),
            "shoot": Animation(speed=2, position=Vector2(0, 32), frames=3, loop=False, agent=self,
                               size=Vector2(32, 19)),
            "reload": Animation(speed=4, position=Vector2(0, 64), frames=8, loop=False, agent=self,
                                size=Vector2(32, 19)),
            "beer": Animation(speed=4, position=Vector2(0, 96), frames=7, loop=False, agent=self,
                              size=Vector2(32, 32)),

        })
        self.__legs = AnimatedSprite(position=Vector2(0, 0), start_anim="idle", name="legs", animations={
            "idle": Animation(speed=7, position=Vector2(0, 19), frames=3, size=Vector2(32, 13)),
            "run": Animation(speed=5, position=Vector2(96, 19), frames=4, size=Vector2(32, 13))
        })
        self.__legs.set_position(Vector2.sum_vector(self.__legs.get_position(), Vector2(0, 19)))

        self.add_child(self.__legs)
        self.add_child(self.__arms)

    def set_anim_free(self, free):
        self.__arms.set_anim_free(free)
        self.__legs.set_anim_free(free)

        if self.__arms.get_current_anim_name() == "reload":
            self.reload()

    def update(self):
        self.check_collision()
        movement, motion = self.move(self.get_position(), self.get_speed())
        self.update_fire_rate()
        self.time_sp()
        if pyxel.btn(pyxel.KEY_SPACE) and self.__arms.is_anim_free():
            if self.can_shoot():
                self.shoot(Vector2(self.get_position().x + 24, self.get_position().y + 14))
                self.__arms.set_current_anim_name("shoot")

            '''elif self.get_ammo() == 0:
                self.__arms.set_current_anim_name("reload")'''

        elif pyxel.btn(pyxel.KEY_R) and self.__arms.is_anim_free() and self.get_ammo() < 7:
            self.__arms.set_current_anim_name("reload")

        elif pyxel.btn(pyxel.KEY_Q) and self.__arms.is_anim_free() and self.get_special() >= 50:
            self.__arms.set_current_anim_name("beer")
            self.active_special()

        self.set_position(movement)
        self.__legs.set_current_anim_name(self.update_anim(motion))

        if self.__arms.is_anim_free():
            self.__arms.set_current_anim_name(self.update_anim(motion))

    def draw(self):

        for i in range(self.get_ammo()):
            pyxel.blt(245 - (7 * i), 128, 0, 224, 6, 7, 13, pyxel.COLOR_PURPLE)

        pyxel.rect(15, 10, 52, 4, 7 if self.get_special() < 50 else pyxel.frame_count % 16)
        pyxel.rect(16, 11, self.get_special(), 2, 2)
        pyxel.blt(2, 5, 0, 232, 7, 11, 12, pyxel.COLOR_PURPLE)

        for node in self.get_children():
            node.draw()
