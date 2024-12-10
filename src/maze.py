import time
from objects import Point, Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.cells = self.__create_cells()

    def __create_cells(self):
        x = self.__x1
        y = self.__y1

        cols = []

        for i in range(0, self.__num_cols):
            for j in range(0, self.__num_rows):
                top_left = Point(x,y)
                bottom_right = Point(x+self.__cell_size_x, y+self.__cell_size_y)
                cell = Cell(top_left, bottom_right, self.__win)
                
                y += self.__cell_size_y
                cols.append(cell)
            y = self.__y1
            x += self.__cell_size_x
            self.cells.append(cols)
            cols = []

        print(f"Created grid.")

        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                self.__draw_cell(i, j)
        

    def __draw_cell(self, i, j):
        self.cells[i][j].draw("black")
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)