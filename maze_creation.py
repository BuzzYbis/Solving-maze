from random import randint
import numpy as np


def gen_maze(lowerBound: int, upperBound: int = None, fitted: bool = True, square: bool = True, swamps_amount: float = 1/6) -> np.array:
    """
        Generate a maze
        :param lowerBound: The minimum width for the maze side if upperBound = None it represent the length of the side of the maze
        :param upperBound: The maximum width for the maze side
        :param fitted: If fitted egal True the maze dimensions will be lowerBound * upperBound or lowerBound * lowerBound if upperBound = None or upperBound * upperBound if upperBound != None fitted = True and sqaure = True
        :param square: Boolean telling we want a square or a rectangular one. If upperbound = None the maze will be square
        :param swamps_amount: Give the proportion of swamp in the maze value by default is 1/6
        :return: The maze in a np.array
    """
    assert 0 <= swamps_amount <= 1

