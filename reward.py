"""Function to allocate the rewards of the MDP"""
import numpy as np
from parameters import SWAMP_REWARD, EXIT_REWARD, NORMAL_REWARD


def reward(pos: [int, int], maze: np.array) -> int:
    """
    Give the reward associated to a position
    :param pos: The position we want the reward of
    :param maze: The maze we are using
    :return: The reward of the given position
    """
    if maze[pos[0]][pos[1]] == "EXIT":
        return EXIT_REWARD
    if maze[pos[0]][pos[1]] == "SWAMP":
        return SWAMP_REWARD
    else:
        return NORMAL_REWARD


def get_neighbors(x: int, y: int, max_x: int, max_y: int) -> list:
    """
    Give the neighbors of the current position
    :param x: The x value of our current position
    :param y: The y value of our current position
    :param max_x: The max possible position on the x-axis
    :param max_y: The max possible position on the y-axis
    :return: The list of the available neighbors
    """
    neighbors = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < max_x and 0 <= ny < max_y:
            neighbors.append((nx, ny))

    return neighbors


def get_reward(currentPos: [int, int], probaMatrix: np.array, maze: np.array) -> int:
    """
    Return the reward from the current position and the probability matrix
    :param currentPos: The current position
    :param probaMatrix: The probability matrix
    :param maze: The maze we are using
    :return: The reward
    """
    x, y = currentPos
    x_max = len(maze)
    y_max = len(maze[0])
    reward = 0
    neighbors = get_neighbors(x, y, x_max, y_max)

    for neighbor in neighbors:
        voisin = probaMatrix[neighbor[0]][neighbor[1]]

        if voisin > 0:
            if maze[neighbor[0]][neighbor[1]] == "SWAMP":
                reward += voisin * SWAMP_REWARD
            elif maze[neighbor[0]][neighbor[1]] == "EXIT":
                reward += voisin * EXIT_REWARD
            else:
                reward += voisin * NORMAL_REWARD

    return reward
