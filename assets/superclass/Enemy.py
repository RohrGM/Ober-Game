import pyxel

from assets.util import Vector2, BodyMoviment
from assets.Enums import Direction
from assets.interfaces import IOnPyxel, IEnemyEvents
from assets.packageScene.CollisionBody import CollisionBody
from assets.packageScene.HitMark import HitMark
from assets.packageScene.AnimatedSprite import AnimatedSprite


class Enemy(IOnPyxel, IEnemyEvents):

    def __init__(self, position: Vector2, zombie_name: str, critical_area: int, rect_size: Vector2) -> None:
        self.__position = position
        self.__life = 10
        self.__speed = 1
        self.__critical_area = critical_area
        self.__elements = []
        self.__anim_locked = False
        self.__body_anim = AnimatedSprite(Vector2(-14, 0), "run", zombie_name, ["run", "attack", "dead"], self.__position)
        self.__collision_body = CollisionBody(self, 1, 0, rect_size, self.__position, "Enemy")

        self.__events = {"dead": []}

        self.__collision_body.add_subscriber(self.on_collision_body, "collision_body")
        self.__body_anim.add_subscriber(self.anim_finished, "animation_finished")
        self.__body_anim.add_subscriber(self.anim_locked, "locked_animation")

        self.__elements.append(self.__collision_body)
        self.__elements.append(self.__body_anim)

    def update_anim(self, new_anim: str) -> None:
        if self.__anim_locked is False or new_anim == "dead":
            self.__body_anim.set_current_anim(new_anim)

    def get_position(self) -> Vector2:
        return self.__position

    def anim_finished(self, animation: str) -> None:
        if animation == "dead":
            self.dead_event(self)

    def anim_locked(self, state: bool) -> None:
        self.__anim_locked = state

    def remove_element(self, element: object) -> None:
        self.__elements.remove(element)

    def get_critical_area(self) -> int:
        return self.__critical_area

    def take_damage(self, damage: float, pos_hit: int) -> None:
        self.__life -= damage
        hit_mark = HitMark(True if pos_hit < self.__critical_area else False, pos_hit, self.__position)
        hit_mark.add_subscriber(self.remove_element, "dead")

        self.__elements.append(hit_mark)
        if self.__life <= 0:
            self.dead()

    def dead(self) -> None:
        self.update_anim("dead")
        self.__collision_body.stop_collision()

    def on_collision_body(self, agent: object, name: str,  pos_y: int) -> None:
        if name == "Barricade":
            self.update_anim("attack")
            if pyxel.frame_count % 50 == 0:
                agent.take_damage(1)

    def dead_event(self, agent: object) -> None:
        for func in self.__events["dead"]:
            func(agent)

    def add_subscriber(self, func, event_name) -> None:
        self.__events[event_name].append(func)

    def remove_subscriber(self, func, event_name) -> None:
        self.__events[event_name].remove(func)

    def update(self) -> None:
        for e in self.__elements:
            e.update()

        if self.__anim_locked is False:
            self.update_anim("run")
            BodyMoviment.simple_moviment(self.__position, Direction.LEFT, self.__speed)

        if self.__position.x < -50:
            self.dead()

    def draw(self) -> None:
        for e in self.__elements:
            e.draw()
