import numpy as np
from random import randint

actions = ["up", "down", "left", "right"]
states = ["good", "swamp", "exit"]
eps = 0.01


def reward(state: str) -> int:
    """
        reward func
        :param state: the current state
        :return: an int 0 if we are on a good tile, 1 if we are at the exit tile and -1 if we are in a swamp
    """
    return int(state == "exit") if state != "swamp" else -1


def state(pos: [int, int], exit_pos: [int, int], maze: np.array) -> str:
    """
        position state
        :param pos: the position of the player
        :param exit_pos: the position of the exit
        :param maze: the array of the maze
        :return: the string of the state of the pos
    """
    return "exit" if pos == exit_pos else "swamp" if maze[pos[0]][pos[1]] == 1 else "good"


def matrix_norm(m1: np.array, m2: np.array):
    """
        compute the norm between two matrix
    """
    return np.linalg.norm(m1 - m2)


