"""Compute the value matrix"""
import numpy as np
from proba import proba_matrix
from reward import get_neighbors, get_reward
from parameters import ACTIONS, EPSILON, GAMMA


def value_matrix(Vt: np.array, nb_iter: int, maze: np.array) -> np.array:
    """
    Compute the value matrix recursively
    :param Vt: The previous value matrix
    :param nb_iter: The number of iteration (for the recursion)
    :param maze: The maze we are using
    :return: The value matrix
    """
    x_max = len(maze) - 1
    y_max = len(maze[0]) - 1

    Vt1 = np.zeros((x_max + 1, y_max + 1))

    for i in range(x_max + 1):
        for j in range(y_max + 1):
            newV = 0
            pos = [i, j]

            for action in ACTIONS:
                result_matrix = proba_matrix(pos, action, maze)
                # sum of p_fd(a_fk) * V_t(d) where f is the state (i,j) and d = (r,c) is the neighbor's state
                sum_element = 0
                neighbors = get_neighbors(i, j, x_max, y_max)

                for neighbor in neighbors:
                    voisin = result_matrix[neighbor[0]][neighbor[1]]
                    sum_element += voisin * Vt[neighbor[0]][neighbor[1]]

                # compute V_t+1(i) for 1 action
                tmpV = get_reward((i, j), result_matrix, maze) + GAMMA * sum_element
                # action that maximize V_t+1(i) for (i,j)
                newV = max(newV, tmpV)

            Vt1[i][j] = newV

    # compute the norm in order to check the return condition
    norme = sum([abs(Vt1[i][j] - Vt[i][j]) for i in range(x_max+1) for j in range(y_max+1)])

    if norme < EPSILON * (1 - GAMMA) / (2 * GAMMA):
        return Vt1, nb_iter + 1
    else:
        return value_matrix(Vt1, nb_iter + 1, maze)
