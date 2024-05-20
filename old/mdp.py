from maze import *
import numpy as np
from random import randint

actions = ["haut", "bas", "gauche", "droite"]

etats = ["ok", "marécage", "arrivée"]

epsilon = 0.01

#fonction de récompense
def recompense(etat):
    if etat == "arrivée":
        return 1
    elif etat == "marécage":
        return -1
    else:
        return 0

#différents "états" d'une position
def etat(s, maze, sgoal):
    if s[0] == sgoal[0] and s[1] == sgoal[1]:
        return "arrivée"
    elif maze[s[0]][s[1]] == 1:
        return "marécage"
    else:
        return "ok"

#actions possibles en fonction de la position (si on est sur les contours)
def actions_possibles(s, maze):
    contour_ligne = len(maze)-1
    contour_colonne = len(maze[0])-1
    c = []
    if s[0] != 0 :
        c.append("haut")
    if s[0] != contour_ligne:
        c.append("bas")
    if s[1] != 0:
        c.append("gauche")
    if s[1] != contour_colonne:
        c.append("droite")
    return c

#probabilité de transition
def p(s,a,sprime, maze) :
    act = actions_possibles(s, maze)

    if a not in act:
        return 0

    else:
        if a == "haut":
            if not "gauche" in act or not "droite" in act: #si on est sur un bord
                if sprime[0] == s[0]-1 and sprime[1] == s[1]:
                    return 0.9
            if sprime[0] == s[0]-1 and sprime[1] == s[1]: #sinon
                return 0.8
            if sprime[0] == s[0]-1 and sprime[1] == s[1]-1: #si vent
                return 0.1
            if sprime[0] == s[0]-1 and sprime[1] == s[1]+1: #si vent
                return 0.1
            else:
                return 0

        if a == "bas":
            if not "gauche" in act or not "droite" in act:
                if sprime[0] == s[0]+1 and sprime[1] == s[1]:
                    return 0.9
            if sprime[0] == s[0]+1 and sprime[1] == s[1]:
                return 0.8
            if sprime[0] == s[0]+1 and sprime[1] == s[1]-1:
                return 0.1
            if sprime[0] == s[0]+1 and sprime[1] == s[1]+1:
                return 0.1
            else:
                return 0

        if a == "gauche":
            if not "haut" in act or not "bas" in act:
                if sprime[0] == s[0] and sprime[1] == s[1]-1:
                    return 0.9
            if sprime[0] == s[0] and sprime[1] == s[1]-1:
                return 0.8
            if sprime[0] == s[0]-1 and sprime[1] == s[1]-1:
                return 0.1
            if sprime[0] == s[0]+1 and sprime[1] == s[1]-1:
                return 0.1
            else:
                return 0

        if a == "droite":
            if not "haut" in act or not "bas" in act:
                if sprime[0] == s[0] and sprime[1] == s[1]+1:
                    return 0.9
            if sprime[0] == s[0] and sprime[1] == s[1]+1:
                return 0.8
            if sprime[0] == s[0]-1 and sprime[1] == s[1]+1:
                return 0.1
            if sprime[0] == s[0]+1 and sprime[1] == s[1]+1:
                return 0.1
            else:
                return 0


#fonction de Bellman
def bellman(s, V, s_e, maze):
    b = []
    act = actions_possibles(s, maze) #on récupère les actions possibles
    for a in actions:
        if a in act:
            b0 = 0
            for sprime in s_e:
                b0 += p(s,a,sprime, maze)*V[sprime[0]][sprime[1]] #on calcule la somme qui se trouve dans le max
            b.append(b0)
    return b

#matrice des états (i,j,état)
def s_etats(maze, sgoal):
    mat_s = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            mat_s.append((i,j,etat((i,j), maze, sgoal)))
    return mat_s

#norme de différence entre deux matrices
def norme(V1, V2):
    return np.linalg.norm(V1-V2)

#fonction d'itération sur les valeurs
def value_iteration(epsilon, gamma, maze, sgoal):
    V = np.zeros((len(maze), len(maze[0])), dtype = float)
    mat_s = s_etats(maze, sgoal)
    while True:
        delta = 0
        Vprime = V.copy()
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                s = (i, j, etat((i, j), maze, sgoal))
                Vprime[i][j] = recompense(s[2]) + gamma*max(bellman(s, V, mat_s,maze)) #equation de Bellman
        delta = norme(V, Vprime)
        if delta < epsilon*(1-gamma)/(2*gamma): #condition d'arrêt
            break
        else:
            V = Vprime
    return V

#fonction de politique optimale
def politique_optimale(s, V, maze, sgoal):
    mat_s = s_etats(maze, sgoal)
    b = []
    for a in actions:
        b0 = 0
        for sprime in mat_s:
            b0 += p(s,a,sprime,maze)*V[sprime[0]][sprime[1]]
        b.append(b0)
    return np.argmax(b)

#fonction du plan optimal
def markov_decision_process(epsilon, gamma, maze, sgoal):
    V = value_iteration(epsilon, gamma, maze, sgoal)
    politique_opt = np.zeros((len(maze), len(maze[0])))
    actions_opti = [["o" for i in range(len(maze[0]))] for j in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            s = (i, j, etat((i, j), maze, sgoal))
            politique_opt[i][j] = politique_optimale(s, V, maze, sgoal) #matrice des actions (int)
            actions_opti[i][j] = actions[int(politique_opt[i][j])] #matrice des actions (lettre)
    return V, politique_opt, actions_opti

#fonction de transition avec l'action a à l'état s
def transition(s, a, maze, sgoal):
    contour_ligne = len(maze)-1
    contour_colonne = len(maze[0])-1
    c = []
    if s[0] == 0 :
        c.append("haut")
    if s[0] == contour_ligne:
        c.append("bas")
    if s[1] == 0:
        c.append("gauche")
    if s[1] == contour_colonne:
        c.append("droite")

    if a in c:
        return s

    else :

        if a == "haut" :
            proba = randint(1, 10) #on calcule la probabilité de vent
            if proba == 1:
                if "gauche" in c: #si on peut pas aller à gauche
                    suivant = (s[0]-1, s[1])
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else : #sinon vent
                    suivant = (s[0]-1, s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            if proba == 2:
                if "droite" in c: #si on peut pas aller à droite
                    suivant = (s[0]-1, s[1])
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else : #sinon vent
                    suivant = (s[0]-1, s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            else: #pas de vent
                suivant = (s[0]-1, s[1])
                s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                return s

        if a == "bas" :
            proba = randint(1, 10)
            if proba == 1:
                if "gauche" in c:
                    suivant = (s[0]+1, s[1])
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else :
                    suivant = (s[0]+1, s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            if proba == 2:
                if "droite" in c:
                    suivant = (s[0]+1, s[1])
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else :
                    suivant = (s[0]+1, s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            else:
                suivant = (s[0]+1, s[1])
                s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                return s

        if a == "gauche" :
            proba = randint(1, 10)
            if proba == 1:
                if "haut" in c:
                    suivant = (s[0], s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else :
                    suivant = (s[0]-1, s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            if proba == 2:
                if "bas" in c:
                    suivant = (s[0], s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else :
                    suivant = (s[0]+1, s[1]-1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            else:
                suivant = (s[0], s[1]-1)
                s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                return s

        if a == "droite" :
            proba = randint(1, 10)
            if proba == 1:
                if "haut" in c:
                    suivant = (s[0], s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return  s
                else :
                    suivant = (s[0]-1, s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            if proba == 2:
                if "bas" in c:
                    suivant = (s[0], s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
                else :
                    suivant = (s[0]+1, s[1]+1)
                    s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                    return s
            else:
                suivant = (s[0], s[1]+1)
                s = (suivant[0], suivant[1], etat(suivant, maze, sgoal))
                return s

#calcul chemin optimal
def chemin_optimal(s0, sgoal, act, maze):
    chemin = []
    s = s0
    chemin.append(s) #on par de s0
    while s != sgoal: #tant qu'on est pas arrivé
        suivant = transition(s, act[s[0]][s[1]], maze, sgoal) #on fait la transition avec l'action optimale
        #on regarde si le robot est en diagonale par rapport a s
        if abs(s[0]-suivant[0]) == 1 and abs(s[1]-suivant[1]) == 1:
            chemin.append("vent")
        s = suivant
        chemin.append(s) #on ajoute la position à la liste
    return chemin


#maze_pdf = np.array([[0, 0, 0, 0, 0],
#                 [0, 1, 1, 1, 0],
#                 [0, 0, 0, 1, 0],
#                 [0, 0, 0, 1, 0],
#                 [0, 0, 0, 0, 0]])

#s0 = (4, 1, "ok")
#sgoal = (0, 3, "arrivée")

#gamma = 0.9

#test = markov_decision_process(epsilon, gamma, maze_pdf, sgoal)
#print(test[0])
#print(test[1])
#print(test[2])
#print(chemin_optimal(s0, sgoal, test[2], maze_pdf))
