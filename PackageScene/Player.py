from PackageScene.AnimatedSprite import AnimatedSprite
from PackageScene.PlayerSpecial import PlayerSpecial
from PackageScene.PlayerWeapon import PlayerWeapon
from Util.ChildrenManager import ChildrenManager
from Util.AnimationData import AnimationData
from Util.CollisionBody import CollisionBody
from Interfaces.IBody2D import IBody2D
from Interfaces.INode2D import INode2D
from Util.Vector2 import Vector2
from typing import Type

import pyxel


class Player(IBody2D):

    def __init__(self, position: Vector2 = Vector2(10, 75), rect_size: Vector2 = Vector2(14, 28), name: str = "Player") -> None:
        self.__children_manager = ChildrenManager(self)
        self.__collision_body = CollisionBody(agent=self, layer=99, mask=99, rect_size=rect_size)
        self.__weapon = PlayerWeapon(position=Vector2(0, 0), max_ammo=7, fire_rate=20, damage=1)
        self.__position = position
        self.__rect_size = rect_size
        self.__name = name
        self.__special = PlayerSpecial()

        self.__arms = AnimatedSprite(position=Vector2(0, 0), start_anim="arms_idle", animations=AnimationData.get_anim_list(
            "player_1", ["arms_idle", "arms_run", "arms_shoot", "arms_reload", "arms_beer"], self))

        self.__legs = AnimatedSprite(position=Vector2(0, 19), start_anim="legs_idle", animations=AnimationData.get_anim_list(
            "player_1", ["legs_idle", "legs_run"], self))

        self.add_child(self.__legs)
        self.add_child(self.__arms)
        self.add_child(self.__weapon)
        self.add_child(self.__special)

    def is_anim_free(self) -> bool:
        if self.__legs.is_anim_free() and self.__arms.is_anim_free():
            return True
        return False

    def get_special(self) -> int:
        return self.__weapon.get_critical_count()

    def on_body_collision(self, body: object, pos_y: int) -> None:
        pass

    def get_rect_size(self) -> Vector2:
        return self.__rect_size

    def add_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.add_child(child)

    def remove_child(self, child: Type[INode2D]) -> None:
        self.__children_manager.remove_child(child)

    def add_parent(self, parent: Type[INode2D]) -> None:
        self.__children_manager.add_parent(parent)

    def get_parent(self) -> Type[INode2D]:
        return self.__children_manager.get_parent()

    def remove_parent(self) -> None:
        self.__children_manager.remove_parent()

    def get_children(self) -> list:
        return self.__children_manager.get_children()

    def set_children(self, children: list) -> None:
        self.__children_manager.set_children(children)

    def get_position(self) -> Vector2:
        if self.__children_manager.get_parent() is None:
            return self.__position
        return Vector2.sum_vector(self.__children_manager.get_parent().get_position(), self.__position)

    def set_position(self, position: Vector2) -> None:
        self.__position = position

    def get_name(self) -> str:
        return self.__name

    def queue_free(self) -> None:
        if self.__children_manager.get_parent() is not None:
            self.__children_manager.get_parent().remove_child(self)

        self.__collision_body.stop_collision()

    def update(self) -> None:
        self.__collision_body.check_collisions()
        movement, motion = self.move(self.get_position())
        self.__weapon.update_fire_rate_time()

        if pyxel.btn(pyxel.KEY_SPACE) and self.__arms.is_anim_free():
            if self.__weapon.shoot(Vector2.sum_vector(self.get_position(), Vector2(24, 14)), self.get_parent()):
                self.update_anim("shoot")

        elif pyxel.btn(pyxel.KEY_R) and self.__arms.is_anim_free() and self.__weapon.can_reload():
            self.update_anim("reload")

        elif pyxel.btn(pyxel.KEY_Q) and self.__arms.is_anim_free() and self.get_special() >= 50:
            self.__arms.set_current_anim_name("beer")

        self.set_position(movement)
        self.update_anim("idle" if motion == 0 else "run")

    def draw(self) -> None:
        '''pyxel.rect(15, 10, 52, 4, 7 if self.get_special() < 50 else pyxel.frame_count % 16)
        pyxel.rect(16, 11, self.get_special(), 2, 2)
        pyxel.blt(2, 5, 0, 232, 7, 11, 12, pyxel.COLOR_PURPLE)'''

        for node in self.get_children():
            node.draw()

    def set_anim_free(self, free) -> None:
        self.__arms.set_anim_free(free)
        self.__legs.set_anim_free(free)

        if self.__arms.get_current_anim_name() == "arms_reload":
            self.__weapon.reload()
        elif self.__arms.get_current_anim_name() == "arms_beer":
            self._active_special()


    def update_anim(self, new_anim: str) -> None:
        if self.__arms.is_anim_free() and self.__arms.is_anim_valid("arms_"+new_anim):
            self.__arms.set_current_anim_name("arms_"+new_anim)

        if self.__legs.is_anim_free() and self.__legs.is_anim_valid("legs_"+new_anim):
            self.__legs.set_current_anim_name("legs_"+new_anim)

    @staticmethod
    def move(position: Vector2, speed: int = 1) -> None:
        motion = 0
        if pyxel.btn(pyxel.KEY_W):
            position.y -= speed
            motion = 1

        if pyxel.btn(pyxel.KEY_S):
            position.y += speed
            motion = 1

        if pyxel.btn(pyxel.KEY_D):
            position.x += speed
            motion = 1

        if pyxel.btn(pyxel.KEY_A):
            position.x -= speed
            motion = -1

        position.y = max(position.y, 50)
        position.y = min(position.y, 110)
        position.x = max(position.x, 0)
        position.x = min(position.x, 25)
        return position, motion
