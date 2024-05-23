"""Compute the path that solve our maze"""
import numpy as np
from random import choices
from reward import reward, get_neighbors


def wind_move(pos: [int, int], action: str, maze_shape: tuple[int, int]) -> tuple:
    """
    Return a move made without wind
    :param maze_shape: The size of the maze shape
    :param pos: The current position
    :param action: The action to follow
    :return: The next position
    """
    possible = get_neighbors(pos[0], pos[1], maze_shape[1], maze_shape[0])

    match action:
        case 'UP':
            if (pos[0] - 1, pos[1] + 1) in possible and (pos[0] - 1, pos[1] - 1) in possible:
                landing = [pos[1], pos[1] + 1, pos[1] - 1]
                weight = [0.8, 0.1, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] - 1, pos[1] + 1) in possible and not (pos[0] - 1, pos[1] - 1) in possible:
                landing = [pos[1], pos[1] + 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] - 1, pos[1] - 1) in possible and not (pos[0] - 1, pos[1] + 1) in possible:
                landing = [pos[1], pos[1] - 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            else:
                winded = pos[1]

            return pos[0] - 1, winded
        case 'DOWN':
            if (pos[0] + 1, pos[1] + 1) in possible and (pos[0] + 1, pos[1] - 1) in possible:
                landing = [pos[1], pos[1] + 1, pos[1] - 1]
                weight = [0.8, 0.1, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] + 1, pos[1] + 1) in possible and not (pos[0] + 1, pos[1] - 1) in possible:
                landing = [pos[1], pos[1] + 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] + 1, pos[1] - 1) in possible and not (pos[0] + 1, pos[1] + 1) in possible:
                landing = [pos[1], pos[1] - 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            else:
                winded = pos[1]

            return pos[0] + 1, winded
        case 'LEFT':
            if (pos[0] + 1, pos[1] - 1) in possible and (pos[0] - 1, pos[1] - 1) in possible:
                landing = [pos[0], pos[0] + 1, pos[0] - 1]
                weight = [0.8, 0.1, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] + 1, pos[1] - 1) in possible and not (pos[0] - 1, pos[1] - 1) in possible:
                landing = [pos[0], pos[0] + 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] - 1, pos[1] - 1) in possible and not (pos[0] + 1, pos[1] - 1) in possible:
                landing = [pos[0], pos[0] - 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            else:
                winded = pos[0]

            return winded, pos[1] - 1
        case 'RIGHT':
            if (pos[0] + 1, pos[1] + 1) in possible and (pos[0] - 1, pos[1] + 1) in possible:
                landing = [pos[0], pos[0] + 1, pos[0] - 1]
                weight = [0.8, 0.1, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] + 1, pos[1] + 1) in possible and not (pos[0] - 1, pos[1] + 1) in possible:
                landing = [pos[0], pos[0] + 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            elif (pos[0] - 1, pos[1] + 1) in possible and not (pos[0] + 1, pos[1] + 1) in possible:
                landing = [pos[0], pos[0] - 1]
                weight = [0.9, 0.1]

                winded = choices(landing, weight)[0]
            else:
                winded = pos[0]

            return winded, pos[1] + 1


def move(pos: [int, int], action: str, maze_shape: tuple[int, int]) -> tuple:
    """
    Return a move made without wind
    :param maze_shape: The size of the maze shape
    :param pos: The current position
    :param action: The action to follow
    :return: The next position
    """
    match action:
        case 'UP':
            return pos[0] - 1, pos[1]
        case 'DOWN':
            return pos[0] + 1, pos[1]
        case 'LEFT':
            return pos[0], pos[1] - 1
        case 'RIGHT':
            return pos[0], pos[1] + 1


def path(optimal_policy: np.array, maze: np.array, start: [list], end: [list], wind: bool = True) -> tuple:
    """
    Compute the used path following the optimal policy
    :param end: The exit position
    :param start: The start position
    :param maze: The maze we are using
    :param wind: True if you want to consider the wind blowing, false if you don't
    :param optimal_policy: The optimal policy matrix
    :return: The optimal path, the action to do in order to follow this path, the total reward after using this path
    """
    used_path, actions, final_reward = [], [], 0
    currentPos = tuple(start)

    if wind:
        moving = wind_move
    else:
        moving = move

    while currentPos != tuple(end):
        used_path.append(currentPos)
        action = optimal_policy[currentPos[0]][currentPos[1]]
        actions.append(action)

        currentPos = moving(currentPos, action, maze.shape)

        final_reward += reward(currentPos, maze)

    used_path.append(currentPos)

    return used_path, actions, final_reward
