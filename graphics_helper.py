from graphics import *

def draw_text(win, message, size=20, y_offset=0):
    text = Text(Point(300, 200 + y_offset), message)
    text.setSize(size)
    text.draw(win)
    return text

def clear_window(win):
    for item in win.items[:]:
        item.undraw()
