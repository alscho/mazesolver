from tkinter import Tk, BOTH, Canvas
from objects import Line, Cell

class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg = "white", height = height, width = width)
        self._canvas.pack(fill = BOTH, expand = 1)
        self._is_running = False
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()

        print("Window closed...")
    
    def close(self):
        self._is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)
