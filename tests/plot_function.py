"""Test of the plotting function"""
from plotting import plot
from maze_creation import gen_maze


maze, start, end = gen_maze(5, [4, 1], [0, 3], swamps_index=[[1, 1], [1, 2], [1, 3], [2, 3], [3, 3]])
V = [[37.358352104209615, 42.03563722560694, 47.283410163799566, 42.17814418640631, 47.283410163799566], [34.04345272432705, 37.88339757617047, 42.623275814629515, 46.8792578133091, 43.09557537906685], [30.884682658172878, 33.61462846350312, 37.31737774119906, 40.56774240262787, 39.02652942985461], [28.041889684447966, 30.340698099278356, 33.444905521227746, 35.27970634489954, 35.162565824031375], [25.444573642950548, 27.37909436960388, 29.886148544872633, 30.77604115901363, 31.556832058119017]]
P = [['RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'LEFT'], ['UP', 'UP', 'UP', 'UP', 'UP'], ['UP', 'RIGHT', 'UP', 'UP', 'UP'], ['UP', 'UP', 'UP', 'UP', 'UP'], ['UP', 'UP', 'UP', 'UP', 'UP']]
chemin_th = [(4, 1), (3, 1), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3)]
chemin = [(4, 1), (3, 1), (2, 1), (2, 2), (1, 2), (0, 3)]

# plot only the maze
plot(maze=maze, name="maze")

# plot the final values matrix
plot(maze=maze, name="values_matrix", V=V)

# plot the policy matrix
plot(maze=maze, name="policy_matrix", P=P)

# plot the path matrix
plot(maze=maze, name="path", OP=chemin_th, UP=chemin)
