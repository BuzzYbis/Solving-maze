import unittest
from maze_creation import gen_maze


class CreateMaze(unittest.TestCase):
    def test_creation_square_onlyPos(self):
        maze, start, end = gen_maze(10, [0, 1], [8, 9])

        self.assertEqual(maze.shape, (10, 10))
        self.assertEqual(maze[0, 1], "START")
        self.assertEqual(maze[8, 9], "EXIT")

    def test_creation_rectangle_onlyPos(self):
        maze, start, end = gen_maze(10, [0, 1], [8, 9], 20)

        self.assertEqual(maze.shape, (10, 20))
        self.assertEqual(maze[0, 1], "START")
        self.assertEqual(maze[8, 9], "EXIT")

    def test_creation_square_notRandom(self):
        maze, start, end = gen_maze(10, [0, 1], [8, 9], swamps_index=[[2, 3], [4, 7]])

        self.assertEqual(maze.shape, (10, 10))
        self.assertEqual(maze[0, 1], "START")
        self.assertEqual(maze[8, 9], "EXIT")
        self.assertEqual(maze[2, 3], "SWAMP")
        self.assertEqual(maze[4, 7], "SWAMP")


if __name__ == '__main__':
    unittest.main()
