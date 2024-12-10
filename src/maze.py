import time, random
from objects import Point, Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        if seed != None:
            self.seed = random.seed(seed)
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def solve(self):
        print("Trying to solve maze")
        return self.solve_r(0, 0)
    
    def solve_direction(self, current, new_x, new_y):
        current.draw_move(self._cells[new_x][new_y])
        result = self.solve_r(new_x, new_y)
        print(f"result: {result}")
        if result:
            time.sleep(5)
            return True
        else:
            current.draw_move(self._cells[new_x][new_y], undo = True)


    def solve_r(self, i, j):
        self._animate()
        print(f"Doing something at i: {i}, j: {j}.")
        current = self._cells[i][j]
        current.visited = True
        #print(f"Doing something at i: {i}, j: {j}.\n Top: {current.has_top_wall}, visited: {self._cells[i-1][j].visited}\nBottom: {current.has_bottom_wall}, visited: {self._cells[i+1][j].visited}\nLeft: {current.has_left_wall}, visited: {self._cells[i][j-1].visited}\nRight: {current.has_right_wall}, visited: {self._cells[i][j+1].visited}")
        if (i == len(self._cells)-1) and (j == len(self._cells[0])-1):
            print("Done.")
            return True
        if i != 0 and current.has_top_wall == False and self._cells[i-1][j].visited == False:
            print("Trying up.")
            new_x = i-1
            new_y = j
            self.solve_direction(current, new_x, new_y)

        if (i != self._num_rows - 1) and current.has_bottom_wall == False and self._cells[i+1][j].visited == False:
            print("Trying down.")
            new_x = i+1
            new_y = j
            self.solve_direction(current, new_x, new_y)

        if j != 0 and current.has_left_wall == False and self._cells[i][j-1].visited == False:
            print("Trying left.")
            new_x = i
            new_y = j-1
            self.solve_direction(current, new_x, new_y)

        if (j != self._num_cols - 1) and current.has_right_wall == False and self._cells[i][j+1].visited == False:
            print("Trying right.")
            new_x = i
            new_y = j+1
            self.solve_direction(current, new_x, new_y)

        print(f"Done at i: {i}, j: {j}")
        return False

    def _break_walls_r(self, i, j):
        if len(self._cells) == 0 or len(self._cells[0]) == 0:
            return
        self._cells[i][j].visited = True
        while True:
            indexes = []
            if i != 0 and self._cells[i-1][j].visited == False:
                indexes.append((i-1, j, "up"))
            if (i != self._num_rows - 1) and self._cells[i+1][j].visited == False:
                indexes.append((i+1, j, "down"))
            if j != 0 and self._cells[i][j-1].visited == False:
                indexes.append((i, j-1, "left"))
            if (j != self._num_cols - 1) and self._cells[i][j+1].visited == False:
                indexes.append((i, j+1, "right"))

            if len(indexes) == 0:
                self._draw_cell(i, j)
                return
        
            rand = random.randrange(len(indexes))

            next_x, next_y, direction = indexes[rand]
            next_cell = self._cells[next_x][next_y]

            match (direction):
                case ("up"):
                    self._cells[i][j].has_top_wall = next_cell.has_bottom_wall = False
                case ("down"):
                    self._cells[i][j].has_bottom_wall = next_cell.has_top_wall = False
                case ("right"):
                    self._cells[i][j].has_right_wall = next_cell.has_left_wall = False
                case ("left"):
                    self._cells[i][j].has_left_wall = next_cell.has_right_wall = False

            self._break_walls_r(next_x, next_y)

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[0])):
                self._cells[i][j].visited = False

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0 or len(self._cells[0]) == 0:
            return
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_rows -1, self._num_cols -1)

    def _create_cells(self):
        x = self._x1
        y = self._y1

        cols = []

        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                top_left = Point(x,y)
                bottom_right = Point(x+self._cell_size_x, y+self._cell_size_y)
                cell = Cell(self._win)
                
                y += self._cell_size_y
                cols.append(cell)
            y = self._y1
            x += self._cell_size_x
            self._cells.append(cols)
            cols = []

        print(f"Created grid.")

        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)
        

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        x1 = self._x1 + self._cell_size_x*j
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y*i
        y2 = y1 + self._cell_size_y
        cell.draw(x1, x2, y1, y2, "black")
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)