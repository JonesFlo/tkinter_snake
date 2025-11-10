class SquareEntity:
    def __init__(self, canvas, x, y, size, color="white"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.square_id = None

        self.draw()

    def draw(self):
        # Remove previous square if it exists
        if self.square_id:
            self.canvas.delete(self.square_id)

        x1, y1 = self.x, self.y
        x2, y2 = x1 + self.size, y1 + self.size
        self.square_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)

    def get_position(self):
        return (self.x, self.y)
