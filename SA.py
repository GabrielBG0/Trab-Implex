import numpy as np
import Decoder
import random


def solutionDistance(graph, solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += graph.distanceBetweenVertices(solution[i], solution[i + 1])
    return distance


def randomSolution(graph):
    cities = graph.getAllVerticesIndex().tolist()
    solution = []

    for i in range(len(graph.getAllVerticesIndex())):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution


def run(path, T, distance):

    graph = Decoder.createGraph(path)

    solution = randomSolution(graph)

    # SIMULATED ANNAELING
    custo0 = solutionDistance(graph, solution)

    for i in range(100):

        T = T * distance
        for j in range(500):
            # TROCA DUAS COORDENADAS E PEGA A SOLUÇÃO VIZINHA
            r1, r2 = np.random.randint(0, len(solution), size=2)

            temp = solution[r1]
            solution[r1] = solution[r2]
            solution[r2] = temp

        # GET NOVO CUSTO
        custo1 = solutionDistance(graph, solution)

        if custo1 < custo0:
            custo0 = custo1
        else:
            x = np.random.uniform()
            if x < np.exp((custo0 - custo1) / T):
                custo0 = custo1
            else:
                temp = solution[r1]
                solution[r1] = solution[r2]
                solution[r2] = temp

    return solution, custo0
