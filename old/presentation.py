import maze as m
import mdp as markov
import matplotlib.pyplot as plt
import numpy as np
from random import randint

# Génération aléatoire de labyrinthe (selon les arguments de create_maze)
#maze = m.create_maze(5,5,True,1/5)
#s0 = (randint(0,len(maze)-1),randint(0,len(maze[0])-1), 'ok')
#sgoal = (randint(0,len(maze)-1),randint(0,len(maze[0])-1), 'arrivée')
# on enlève les marécages de l'arrivée
#maze[s0[0]][s0[1]] = 0
#maze[sgoal[0]][sgoal[1]] = 0

# Récupération du labyrinthe du sujet
#maze = markov.maze_pdf
#s0 = markov.s0
#sgoal = markov.sgoal

# utilisation d'un labyrinthe fait main avec les départs et arrivés que l'on désire
maze = [[0, 0, 0, 0, 0],
 [1, 1, 1, 1, 0],
 [1, 0,1, 1, 0],
 [1, 1, 1, 0, 0],
 [0, 0, 0, 0, 1]]
maze = np.array(maze)
s0 = (0,0,"ok")
sgoal = (4,0,"arrivée")


all = markov.markov_decision_process(0.01, 0.9, maze, sgoal) # Récupération de V et de la matrice des politiques. Utilisation de epsilon et gamma
#print( all[0])
#print("policy : ", all[1])
chemin = markov.chemin_optimal(s0, sgoal, all[2], maze) # Récupération du chemin optimal
#print("chemin optimal : ", chemin)

#inverser les couleurs correspondant à la matrice maze
maze = 1 - maze

#afficher le labirynthe avec le départ en vert et l'arrivée en rouge
#afficher l'action optimale pour chaque case (le nom) en blanc sur les cases noires et en noir sur les cases blanches
#afficher le chemin optimal
plt.imshow(maze, cmap='gray')
plt.plot(s0[1], s0[0], 'go', markersize=30)
plt.plot(sgoal[1], sgoal[0], 'ro', markersize=30)
for i in range(len(all[2])):
    for j in range(len(all[2][0])):
        v = "o"
        if all[1][i][j] == 0:
            v = "↑"
        elif all[1][i][j] == 1 :
            v = "↓"
        elif all[1][i][j] == 2 :
            v = "←"
        elif all[1][i][j] == 3 :
            v = "→"
        if maze[i][j] == 0:
            plt.text(j, i, v, color='white', fontsize=15)
        else:
            plt.text(j, i, v, color='black', fontsize=15)

#supprimer "vent" de chemin
chemin = [x for x in chemin if x != "vent"]

#afficher le chemin optimal en ligne bleue
for i in range(len(chemin)):
    plt.plot(chemin[i][1], chemin[i][0], 'bo', markersize=10)
    if i < len(chemin)-1 :
        plt.plot([chemin[i][1], chemin[i+1][1]], [chemin[i][0], chemin[i+1][0]], 'b', linewidth=3)


plt.show()
