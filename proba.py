"""Function to get the probability matrix"""
import numpy as np


def proba_matrix(pos: [int, int], action: str, maze: np.array) -> np.array:
    """
    Return the probability matrix from the position and the chosen action
    :param pos: The given position
    :param action: The chosen action
    :param maze: The maze we are using
    :return: The probability matrix
    """
    x, y = pos
    x_max = len(maze) - 1
    y_max = len(maze[0]) - 1

    matrix = np.zeros((x_max + 1, y_max + 1))

    if action == "UP":
        if x == 0:
            return matrix
        elif (y == 0) and x != 0:
            matrix[x - 1][0] = 0.9
            matrix[x - 1][1] = 0.1
        elif (y == y_max) and x != 0:
            matrix[x - 1][y_max] = 0.9
            matrix[x - 1][y_max - 1] = 0.1
        else:
            matrix[x - 1][y] = 0.8
            matrix[x - 1][y + 1] = 0.1
            matrix[x - 1][y - 1] = 0.1

    elif action == "DOWN":
        if x == x_max:
            return matrix
        elif (y == 0) and x != x_max:
            matrix[x + 1][0] = 0.9
            matrix[x + 1][1] = 0.1
        elif (y == y_max) and x != x_max:
            matrix[x + 1][y_max] = 0.9
            matrix[x + 1][y_max - 1] = 0.1
        else:
            matrix[x + 1][y] = 0.8
            matrix[x + 1][y + 1] = 0.1
            matrix[x + 1][y - 1] = 0.1

    elif action == "LEFT":
        if y == 0:
            return matrix
        elif (x == 0) and y != 0:
            matrix[0][y - 1] = 0.9
            matrix[1][y - 1] = 0.1
        elif (x == x_max) and y != 0:
            matrix[x_max][y - 1] = 0.9
            matrix[x_max - 1][y - 1] = 0.1
        else:
            matrix[x][y - 1] = 0.8
            matrix[x - 1][y - 1] = 0.1
            matrix[x + 1][y - 1] = 0.1

    elif action == "RIGHT":
        if y == y_max:
            return matrix
        elif (x == 0) and y != y_max:
            matrix[0][y + 1] = 0.9
            matrix[1][y + 1] = 0.1
        elif (x == x_max) and y != y_max:
            matrix[x_max][y + 1] = 0.9
            matrix[x_max - 1][y + 1] = 0.1
        else:
            matrix[x][y + 1] = 0.8
            matrix[x - 1][y + 1] = 0.1
            matrix[x + 1][y + 1] = 0.1

    return matrix
