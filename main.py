from ui.game_window import create_game_window
from game_logic.game_loop import run_game_loop

def main():
    window, canvas = create_game_window()
    run_game_loop(window,canvas)

if __name__ == "__main__":
    main()