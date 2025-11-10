from ui.snake import Snake
from ui.food import Food

def run_game_loop(window, canvas):
    cell_size = 20
    grid_width = canvas.winfo_reqwidth() // cell_size
    grid_height = canvas.winfo_reqheight() // cell_size

    # Create snake
    snake = Snake(canvas, x=100, y=100, size=cell_size)

    # Create food and place it on the canvas
    food = Food(
        canvas=canvas,
        grid_width=grid_width,
        grid_height=grid_height,
        size=cell_size,
        snake=snake,
        lifetime_ms=5000  # or whatever value you want
    )

    def game_tick():
        # You can later add logic to check if food was eaten, etc.
        window.after(100, game_tick)

    game_tick()
    window.mainloop()