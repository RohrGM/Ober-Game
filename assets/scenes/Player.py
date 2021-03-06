from assets.util import Vector2, BodyMoviment
from assets.interfaces import IOnPyxel
from assets.packageScene import AnimatedSprite, Weapon


class Player(IOnPyxel):

    def __init__(self, position: Vector2) -> None:
        self.__position = position
        self.__elements = []
        self.__anim_locked = False
        self.__arms_anim = AnimatedSprite(Vector2(0, 0), "arms_idle", "player_0",
                                          ["arms_idle", "arms_run", "arms_shoot", "arms_reload", "arms_special"],
                                          self.__position)
        self.__legs_anim = AnimatedSprite(Vector2(0, 19), "legs_idle", "player_0", ["legs_idle", "legs_run"],
                                          self.__position)
        self.__weapon = Weapon(20, 7, Vector2(0, 14), self.__position, self.__arms_anim, "shotgun")

        self.__arms_anim.add_subscriber(self.anim_locked, "locked_animation")
        self.__weapon.add_subscriber(self.weapon_update_anim, "shoot")
        self.__weapon.add_subscriber(self.weapon_update_anim, "reload")
        self.__weapon.add_subscriber(self.weapon_update_anim, "special")

        self.__elements.append(self.__weapon)
        self.__elements.append(self.__legs_anim)
        self.__elements.append(self.__arms_anim)

    def get_position(self) -> Vector2:
        return self.__position

    def anim_locked(self, state: bool) -> None:
        self.__anim_locked = state

    def weapon_update_anim(self, anim: str) -> None:
        self.update_anim(anim)

    def update_anim(self, new_anim: str) -> None:

        if self.__anim_locked is False:
            self.__arms_anim.set_current_anim("arms_" + new_anim)

        self.__legs_anim.set_current_anim("legs_" + new_anim)

    def update(self) -> None:
        motion = BodyMoviment.control_moviment(self.__position, 1)
        self.update_anim("idle" if motion == 0 else "run")

        for e in self.__elements:
            e.update()

    def draw(self) -> None:
        for e in self.__elements:
            e.draw()
