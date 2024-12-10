class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width = 2
        )
    
class Cell():
    def __init__(self, p1, p2, win = None):
        self.__win = win
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def __repr__(self):
        return f"Cell: '{self.get_coordinates()}', '{self.get_walls()}"

    def get_walls(self):
        walls = []
        if self.has_bottom_wall:
            walls.append("1")
        else:
            walls.append("0")

        if self.has_left_wall:
            walls.append("1")
        else:
            walls.append("0")

        if self.has_right_wall:
            walls.append("1")
        else:
            walls.append("0")

        if self.has_top_wall:
            walls.append("1")
        else:
            walls.append("0")
        return walls

    def get_coordinates(self):
        left_x = min(self.__x1, self.__x2)
        right_x = max(self.__x1, self.__x2)
        top_y = min(self.__y1, self.__y2)
        bottom_y = max(self.__y1, self.__y2)
        return (left_x, top_y), (right_x, bottom_y)
    
    def get_centre(self):
        top_left, bottom_right = self.get_coordinates()
        centre_x = (top_left[0]+bottom_right[0]) // 2
        centre_y = (top_left[1]+bottom_right[1]) // 2
        centre = Point(centre_x, centre_y)
        return centre

    def draw(self, fill_color):
        left_x = min(self.__x1, self.__x2)
        right_x = max(self.__x1, self.__x2)
        top_y = min(self.__y1, self.__y2)
        bottom_y = max(self.__y1, self.__y2)
        top_left = Point(left_x, top_y)
        bottom_left = Point(left_x, bottom_y)
        top_right = Point(right_x, top_y)
        bottom_right = Point(right_x, bottom_y)

        if self.has_top_wall:
            top = Line(top_left, top_right)
            self.__win.draw_line(top, fill_color)
            #top.draw(canvas, fill_color)
        if self.has_bottom_wall:
            bottom = Line(bottom_left, bottom_right)
            self.__win.draw_line(bottom, fill_color)
            #bottom.draw(canvas, fill_color)
        if self.has_left_wall:
            left = Line(bottom_left, top_left)
            self.__win.draw_line(left, fill_color)
            #left.draw(canvas, fill_color)
        if self.has_right_wall:
            right = Line(bottom_right, top_right)
            self.__win.draw_line(right, fill_color)
            #right.draw(canvas, fill_color)

    def draw_move(self, to_cell, undo = False):
        centre1 = self.get_centre()
        centre2 = to_cell.get_centre()

        path = Line(centre1, centre2)

        if undo:
            fill_color = "grey"
        else:
            fill_color = "red"

        self.__win.draw_line(path, fill_color)



