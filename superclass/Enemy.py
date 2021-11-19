from util import Vector2, BodyMoviment
from Enums import Direction
from interfaces import IOnPyxel
from packageScene import AnimatedSprite, CollisionBody


class Enemy(IOnPyxel):

    def __init__(self, position: Vector2, life: int) -> None:
        self.__position = position
        self.__life = life
        self.__speed = 1
        self.__critical_area = 9
        self.__elements = []
        self.__anim_locked = False
        self.__body_anim = AnimatedSprite(Vector2(0, 0), "run", "zombie_1", ["run", "attack", "dead"], self.__position)
        self.__collision_body = CollisionBody(self, 1, 0, Vector2(14, 28), self.__position, "Enemy")

        self.__collision_body.add_subscriber(self.on_collision_body, "collision_body")
        self.__body_anim.add_subscriber(self.anim_finished, "animation_finished")
        self.__body_anim.add_subscriber(self.anim_locked, "locked_animation")

        self.__elements.append(self.__collision_body)
        self.__elements.append(self.__body_anim)

    def update_anim(self, new_anim: str) -> None:
        if self.__anim_locked is False:
            self.__body_anim.set_current_anim(new_anim)

    def anim_finished(self, animation: str) -> None:
        if animation == "dead":
            pass

    def anim_locked(self, state: bool) -> None:
        self.__anim_locked = state

    def get_critical_area(self) -> int:
        return self.__critical_area

    def take_damage(self, damage: float) -> None:
        self.__life -= damage
        if self.__life <= 0:
            self.dead()

    def dead(self) -> None:
        self.update_anim("dead")

    def on_collision_body(self, agent: object, name: str,  pos_y: int) -> None:
        pass

    def update(self) -> None:

        if self.__anim_locked is False:
            BodyMoviment.simple_moviment(self.__position, Direction.LEFT, self.__speed)

        for e in self.__elements:
            e.update()

    def draw(self) -> None:
        for e in self.__elements:
            e.draw()
