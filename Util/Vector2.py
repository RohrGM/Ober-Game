class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def sum_vector(vec1, vec2):
        return Vector2(vec1.x + vec2.x, vec1.y + vec2.y)

