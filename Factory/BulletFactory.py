import pyxel

from Nodes.BasicNodes.Body2D import Body2D
from Util.Vector2 import Vector2


class BulletFactory:

    @staticmethod
    def create(position: Vector2,  agent, specification: str) -> object:

        def on_body_collision_normal(body, pos_y):
            if body.name == "Enemy" and bullet.__valid:
                bullet.__valid = False
                bullet.queue_free()

                if pos_y < body.get_critical_area():
                    bullet.__agent.add_special()
                    body.take_damage(2)
                else:
                    body.take_damage(1)

        def on_body_collision_special(body, pos_y):
            if body.name == "Enemy" and bullet.__valid:

                if pos_y < body.get_critical_area():
                    bullet.__agent.add_special()
                    body.take_damage(2)
                else:
                    body.take_damage(1)

        def update():
            bullet.check_collision()
            bullet.set_position(Vector2(bullet.get_position().x + bullet.get_speed(), bullet.get_position().y))

            if bullet.get_position().x > 256:
                bullet.queue_free()

        def draw_normal():
            pyxel.rect(bullet.get_position().x, bullet.get_position().y, bullet.get_size().x,
                       bullet.get_size().y, 10)

        def draw_special():
            pyxel.rect(bullet.get_position().x, bullet.get_position().y, bullet.get_size().x,
                       bullet.get_size().y, pyxel.frame_count % 16)

        factory_method = {
            "update": update,
            "draw_normal": draw_normal,
            "draw_special": draw_special,
            "on_body_collision_normal": on_body_collision_normal,
            "on_body_collision_special": on_body_collision_special
        }

        bullet = Body2D(position=position, speed=10, size=Vector2(5, 1), layer=0, mask=1, name="Bullet")
        bullet.__valid = True
        bullet.__agent = agent

        bullet.update = factory_method["update"]
        bullet.draw = factory_method["draw_" + specification]
        bullet.on_body_collision = factory_method["on_body_collision_" + specification]

        return bullet
