import random
from .components.square import SquareEntity

class Food(SquareEntity):
    def __init__(self, canvas, grid_width, grid_height, size, snake, lifetime_ms=5000, color="red"):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.snake = snake
        self.lifetime_ms = lifetime_ms
        self.canvas = canvas
        self.size = size
        self.color = color

        # Initial dummy position, will be overwritten
        super().__init__(canvas, 0, 0, size, color)
        self.relocate()

    def relocate(self):
        while True:
            x = random.randint(0, self.grid_width - 1) * self.size
            y = random.randint(0, self.grid_height - 1) * self.size
            if (x, y) not in self.snake.get_positions():
                break

        self.x = x
        self.y = y
        self.draw()

        self.canvas.after(self.lifetime_ms, self.relocate)
