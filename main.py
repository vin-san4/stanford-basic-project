import json
from graphics import *
from graphics_helper import draw_text, clear_window

def load_puzzles(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def show_room(win, puzzle):
    clear_window(win)
    draw_text(win, f"Room {puzzle['room']}", 24, -100)
    draw_text(win, puzzle['question'], 16, -30)
    draw_text(win, "Type your answer below and press Enter", 12, 10)
    
    entry = Entry(Point(300, 250), 20)
    entry.draw(win)
    submit = Text(Point(300, 300), "Press Enter in box to submit")
    submit.setSize(10)
    submit.draw(win)

    while True:
        key = win.getKey()
        if key == "Return":
            answer = entry.getText().strip()
            if answer == puzzle['answer']:
                clear_window(win)
                draw_text(win, "Correct! Proceeding...", 20)
                break
            else:
                clear_window(win)
                draw_text(win, "Incorrect. Try again.", 16)
                return show_room(win, puzzle)

def main():
    win = GraphWin("Mind Maze", 600, 400)
    puzzles = load_puzzles("puzzles.json")

    welcome = draw_text(win, "Welcome to Mind Maze!", 24, -60)
    draw_text(win, "Click anywhere to begin...", 14, 20)
    win.getMouse()
    clear_window(win)

    for puzzle in puzzles:
        show_room(win, puzzle)

    clear_window(win)
    draw_text(win, "Congratulations! You escaped the maze!", 20)
    draw_text(win, "Click anywhere to exit.", 12, 40)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
