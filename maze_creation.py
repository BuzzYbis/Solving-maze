"""Function to generate a maze"""
from random import randint
import numpy as np


def gen_maze(ligne: int, start_pos: [int, int], exit_pos: [int, int], colonne: int = None,
             swamps_amount: float = 1 / 6, swamps_index: list[list] = None, ) -> np.array:
    """
        Generate a maze
        :param colonne: The minimum width for the maze side if ligne = None it represents the length of the side of the maze
        :param start_pos: The position of the beginning of the maze
        :param exit_pos: The position of the exit of the maze
        :param ligne: The maximum width for the maze side
        :param swamps_amount: Give the proportion of swamp in the maze value by default is 1/6
        :param swamps_index: if you want to choose the swamps position give a list of their coordinate and they will not be determined randomly
        :return: The maze in a np.array
    """
    assert 0 <= swamps_amount <= 1

    if swamps_index is None:
        if colonne:
            maze = np.zeros((colonne, ligne), dtype='O')
            nb_swamps = int(colonne * ligne * swamps_amount)
            swamps_index = [(randint(0, colonne - 1), randint(0, ligne - 1)) for _ in range(nb_swamps)]
        else:
            maze = np.zeros((ligne, ligne), dtype='O')
            nb_swamps = int(ligne * ligne * swamps_amount)
            swamps_index = [(randint(0, ligne - 1), randint(0, ligne - 1)) for _ in range(nb_swamps)]

        for s in swamps_index:
            maze[s[0]][s[1]] = "SWAMP"
    else:
        if colonne:
            maze = np.zeros((colonne, ligne), dtype='O')
            nb_swamps = int(colonne * ligne * swamps_amount)
        else:
            maze = np.zeros((ligne, ligne), dtype='O')
            nb_swamps = int(ligne * ligne * swamps_amount)

        for s in swamps_index:
            maze[s[0]][s[1]] = "SWAMP"

    maze[start_pos[0]][start_pos[1]] = "START"
    maze[exit_pos[0]][exit_pos[1]] = "EXIT"

    return maze, start_pos, exit_pos
