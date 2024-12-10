from window import Window
from objects import Line, Point, Cell

def create_grid(win_width, win_height, grid_width, grid_height, win):
    x = grid_width
    y = grid_height

    rows = []
    cols = []

    while y < win_height:
        while x < win_width:
            top_left = Point(x,y)
            bottom_right = Point(x+grid_width, y+grid_height)
            cell = Cell(top_left, bottom_right, win)
            cell.draw("black")
            x += grid_width
            rows.append(cell)
        x = grid_width
        y += grid_height
        cols.append(rows)
        rows = []

    print(f"Created grid.")

    return cols

def test_draw_cell(delta, size, grid_height, grid_width, win):
    
    ### has_bottom_wall, has_left_wall, has_right_wall, has_top_wall
    states = [
        [(0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1)],
        [(0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1)],
        [(1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1)],
        [(1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1)],
    ]

    y = grid_height + delta
    x = grid_width + delta

    for i in range(0,4):
        for j in range (0,4):
            top_left = Point(x,y)
            bottom_right = Point(x+size, y+size)
            cell = Cell(top_left, bottom_right, win)
            cell.has_bottom_wall = states[i][j][0]
            cell.has_left_wall = states[i][j][1]
            cell.has_right_wall = states[i][j][2]
            cell.has_top_wall = states[i][j][3]

            cell.draw("black")

            x+= grid_width
        x = grid_width+ delta
        y += grid_height


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)
    grid_width = 50
    grid_height = 50

    cells = create_grid(win_width, win_height, grid_width, grid_height, win)
 
    cells[0][0].draw_move(cells[0][1])
    
    #delta = 10
    #size = 30
    #test_draw_cell(delta, size, grid_height, grid_width, win)

    win.wait_for_close()
    

main()