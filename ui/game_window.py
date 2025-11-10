import tkinter as tk

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_TITLE = "SNAKE"

def create_game_window():
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    canvas.pack()
    return window, canvas