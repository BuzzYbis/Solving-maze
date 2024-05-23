"""Function to compute the policy matrix"""
import numpy as np
from reward import get_reward, get_neighbors
from proba import proba_matrix
from parameters import ACTIONS


def policy_matrix(value_matrix: np.array, maze: np.array) -> np.array:
    """
        Compute the policy matrix from the value matrix
        :param value_matrix: The value matrix
        :param maze: The used maze
        :return: The policy matrix
    """
    value_size = value_matrix.shape
    policy_mat = np.zeros(value_size, dtype='O')

    for i in range(value_size[0]):
        for j in range(value_size[1]):
            Q = 0
            action = "UP"

            for a in ACTIONS:
                probas = proba_matrix((i, j), a, maze)
                Qa = 0
                reward = get_reward((i, j), probas, maze)
                x_max = len(probas)
                y_max = len(probas[0])
                neighbors = get_neighbors(i, j, x_max, y_max)

                for neighbor in neighbors:
                    if probas[neighbor[0]][neighbor[1]] != 0:
                        Qa += probas[neighbor[0]][neighbor[1]] * value_matrix[neighbor[0]][neighbor[1]]

                Qa = reward + 0.9 * Qa

                if Qa > Q:
                    Q = Qa
                    action = a

            policy_mat[i][j] = action

    return policy_mat
