from .components.square import SquareEntity

class Snake(SquareEntity):
    def __init__(self, canvas, x, y, size=20, color="white"):
        super().__init__(canvas, x, y, size, color)
        self.direction = "Right"  # Default direction
        self.canvas_width = canvas.winfo_reqwidth()
        self.canvas_height = canvas.winfo_reqheight()

    def set_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        if self.direction == "Up":
            self.y -= self.size
        elif self.direction == "Down":
            self.y += self.size
        elif self.direction == "Left":
            self.x -= self.size
        elif self.direction == "Right":
            self.x += self.size

        # Wrap around logic
        if self.x < 0:
            self.x = self.canvas_width - self.size
        elif self.x >= self.canvas_width:
            self.x = 0

        if self.y < 0:
            self.y = self.canvas_height - self.size
        elif self.y >= self.canvas_height:
            self.y = 0
            


        self.draw()  # Redraw at new position

    def get_positions(self):
        return [self.get_position()]