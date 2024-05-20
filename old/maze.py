from random import randint
import numpy as np


def create_maze(lowerBound: int, upperBound: int = None, square: True or False = False,
                swamps_prop: int = 1 / 6) -> np.array:
    if upperBound == None:
        n = lowerBound

        # create the base maze without any swamps in it
        res = np.zeros((n, n))

        # randomly choose position of the swamps 
        nb_swamps = int(n ** 2 * swamps_prop)
        swamps_index = [(randint(0, n - 1), randint(0, n - 1)) for _ in range(nb_swamps)]
    else:
        if square == True:
            n = randint(lowerBound, upperBound)

            # create the base maze without any swamps in it
            res = np.zeros((n, n))

            # randomly choose position of the swamps 
            nb_swamps = int(n ** 2 * swamps_prop)
            swamps_index = [(randint(0, n - 1), randint(0, n - 1)) for _ in range(nb_swamps)]
        else:
            n, m = randint(lowerBound, upperBound), randint(lowerBound, upperBound)

            # create the base maze without any swamps in it
            res = np.zeros((n, m))

            # randomly choose position of the swamps 
            nb_swamps = int(n * m * swamps_prop)
            swamps_index = [(randint(0, n - 1), randint(0, m - 1)) for _ in range(nb_swamps)]

    for c in swamps_index:
        res[c[0]][c[1]] = 1

    return res
