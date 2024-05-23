"""Function to plot the Values, the Policy and the Path"""
import numpy as np
from matplotlib import pyplot as plt


def plot(maze: np.array, name: str = "values_matrix" or "policy_matrix" or "path" or "maze", V: np.array = None, P: np.array = None, OP: np.array = None, UP: np.array = None):
    """
        Display the Values, the Policy and the Path in function of the arg
        :param maze: The maze used to make the computation
        :param name: The name of the fig.
        :param V: The matrix for the values plotting
        :param P: the matrix for the policy plotting
        :param OP: the matrix for the optimal path plotting
        :param UP: the matrix for the used path plotting
    """
    if name == "values_matrix":
        assert V is not None
    if name == "policy_matrix":
        assert P is not None
    if name == "path":
        assert OP is not None
        assert UP is not None

    maze_size = maze.shape
    print(maze_size)

    plt.figure(name, figsize=(15, 15))
    plt.gca().invert_yaxis()

    match name:
        case "values_matrix":
            for i in range(maze_size[0]):
                for j in range(maze_size[1]):
                    plt.text(j, i, round(V[i][j], 2), ha='center', va='center', fontsize=20)

                    if maze[i][j] == "SWAMP":
                        plt.gca().add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fc='gray'))

            plt.title('Matrice des valeurs V final pour chaque état')
        case "policy_matrix":
            for i in range(maze_size[0]):
                for j in range(maze_size[1]):
                    arrow = ''
                    match P[i][j]:
                        case 'UP':
                            arrow = '↑'
                        case 'DOWN':
                            arrow = '↓'
                        case 'LEFT':
                            arrow = '←'
                        case 'RIGHT':
                            arrow = '→'

                    if maze[i][j] == "EXIT":
                        plt.text(j, i, 'EXIT', ha='center', va='center')
                    elif maze[i][j] == "START":
                        plt.text(j, i, arrow + '\nSTART', ha='center', va='center', fontsize=20)
                    else:
                        plt.text(j, i, arrow, ha='center', va='center', fontsize=20)

                    if maze[i][j] == "SWAMP":
                        plt.gca().add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fc='gray'))

            plt.title('Action retenue pour chaque état')
        case "path":
            opt_coords_x, opt_coords_y = [p[1] for p in OP], [p[0] for p in OP]
            used_coords_x, used_coords_y = [p[1] for p in UP], [p[0] for p in UP]

            plt.plot(opt_coords_x, opt_coords_y, marker='X', color='red', label='Optimal path', linestyle='dashed', linewidth=3, markersize=12)
            plt.plot(used_coords_x, used_coords_y, marker='o', color='blue', label='Followed path', linewidth=3, markersize=12)

            for i in range(maze_size[0]):
                for j in range(maze_size[1]):
                    if maze[i][j] == "SWAMP":
                        plt.gca().add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fc='gray'))

                    if maze[i][j] == "EXIT":
                        plt.text(j, i, 'EXIT', ha='center', va='center', fontsize=30)
                    elif maze[i][j] == "START":
                        plt.text(j, i,  'START', ha='center', va='center', fontsize=30)

            plt.title('Chemin optimal et chemin suivi (en prenant en compte le vent)')
            plt.legend()
        case "maze":
            for i in range(maze_size[0]):
                for j in range(maze_size[1]):
                    if maze[i][j] == "SWAMP":
                        plt.gca().add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fc='gray'))

                    if maze[i][j] == "EXIT":
                        plt.text(j, i, 'EXIT', ha='center', va='center', fontsize=30)
                    elif maze[i][j] == "START":
                        plt.text(j, i,  'START', ha='center', va='center', fontsize=30)

    plt.xticks(np.arange(-0.5, maze_size[1] + 0.5))
    plt.yticks(np.arange(-0.5, maze_size[0] + 0.5))
    plt.tick_params(which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)

    plt.grid()

    plt.savefig("img/" + name + ".png")

    plt.show()
