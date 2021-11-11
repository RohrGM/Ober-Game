from Util.Vector2 import Vector2
from Factory.BulletFactory import BulletFactory


class GunFactory:

    @staticmethod
    def create():

        def shoot(self, position: Vector2):
            self.__ammo -= 1

            self.get_parent().add_child(
                BulletFactory.create(position, self, "special" if self.__sp_active else "normal"))
            self.__can_shoot = self.__fire_rate

        def update_fire_rate(self):
            if self.__can_shoot > 0:
                self.__can_shoot -= 1

        def can_shoot(self):
            if self.__can_shoot == 0:
                if self.__ammo > 0:
                    return True
            return False

        gun = object
        gun.__ammo = 7

