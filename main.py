"""Main test"""
import numpy as np
from maze_creation import gen_maze
from value import value_matrix
from policy_matrix import policy_matrix
from path import path
from plotting import plot


if __name__ == "__main__":
    maze, s, e = gen_maze(5, [4, 1], [0, 3], swamps_index=[[1, 1], [1, 2], [1, 3], [2, 3], [3, 3]])

    Vt_f, nb_iter = value_matrix(Vt=np.zeros(maze.shape), nb_iter=0, maze=maze)
    best_policy = policy_matrix(value_matrix=Vt_f, maze=maze)
    optimal_path, action_OP, final_reward_OP = path(optimal_policy=best_policy, maze=maze, start=s, end=e, wind=False)
    used_path, action_UP, final_reward_UP = path(optimal_policy=best_policy, maze=maze, start=s, end=e, wind=True)

    plot(maze=maze, name="maze")
    plot(maze=maze, name="values_matrix", V=Vt_f)
    plot(maze=maze, name="policy_matrix", P=best_policy)
    plot(maze=maze, name="path", OP=optimal_path, UP=used_path)
