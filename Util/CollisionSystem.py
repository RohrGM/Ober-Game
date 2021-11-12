class CollisionSystem:
    collision_layer = []
    collision_mask = []

    @staticmethod
    def add_body_on_system(body):
        CollisionSystem.collision_layer.append(body)
        CollisionSystem.collision_mask.append(body)

    @staticmethod
    def remove_body_on_system(body):
        try:
            CollisionSystem.collision_layer.remove(body)
            CollisionSystem.collision_mask.remove(body)
        except():
            print("Body não encontrado")

    @staticmethod
    def has_colliding(body, other_body):
        if body != other_body and body.get_position().x + body.get_rect_size().x > other_body.get_position().x \
                and other_body.get_position().x + other_body.get_rect_size().x > body.get_position().x \
                and body.get_position().y + body.get_rect_size().y > other_body.get_position().y \
                and other_body.get_position().y + other_body.get_rect_size().y > body.get_position().y:
            return True, body.get_position().y - other_body.get_position().y
        return False, 0
