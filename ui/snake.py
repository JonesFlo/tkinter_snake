from .components.square import SquareEntity

class Snake(SquareEntity):
    def __init__(self, canvas, x, y, size=20, color="white"):
        super().__init__(canvas, x, y, size, color)

    def get_positions(self):
        # For now, just return the head position
        return [self.get_position()]
