import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_reset_cells_visited(self):
        tests = [
            [10, 10],
            [0, 1],
            [1, 0],
            [1, 1],
            [0, 0]
        ]

        for test in tests:
            num_cols = test[0]
            num_rows = test[1]
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

            m1._break_entrance_and_exit()

            m1._break_walls_r(0, 0)

            m1._reset_cells_visited()

        for i in range(0, len(m1._cells)):
            for j in range(0, len(m1._cells[0])):
                self.assertFalse(m1._cells[i][j])

    def text_maze_break_entrance_and_exit(self):
        tests = [
            [10, 10],
            [0, 1],
            [1, 0],
            [1, 1],
            [0, 0]
        ]

        for test in tests:
            num_cols = test[0]
            num_rows = test[1]
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

            m1._break_entrance_and_exit()

            self.assertFalse(m1._cells[0][0].has_top_wall)
            self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_maze_create_cells(self):
        tests = [
            [12, 10],
            [1, 1],
            [0, 10],
            [1, 0],
            [100, 100],
        ]

        for test in tests:
            num_cols = test[0]
            num_rows = test[1]
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            if len(m1._cells) > 0:
                self.assertEqual(
                    len(m1._cells[0]),
                    num_rows,
                )

if __name__ == "__main__":
    unittest.main()