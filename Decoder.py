import numpy as np
import math


def generateVector(path):
    vector = np.loadtxt(path, dtype=int, delimiter=' ')

    return vector


def createGraph(path):
    vector = generateVector(path)

    graph = Graph(vector)

    return graph


class Graph:
    def __init__(self, vector):
        self.vector = vector

    def distanceBetweenVertices(self, v1, v2):
        coordsV1 = [self.vector[v1 - 1][1], self.vector[v1 - 1][2]]
        coordsV2 = [self.vector[v2 - 1][1], self.vector[v2 - 1][2]]
        d = math.sqrt(((coordsV1[0] - coordsV2[0]) ** 2) +
                      ((coordsV1[1] - coordsV2[1]) ** 2))
        return d

    def getVerticeCoords(self, v):
        result = []
        for x_axis in range(v):
            for y_axis in range(v):
                result.append((x_axis, y_axis))
        return result

    def getAllVerticesIndex(self):
        return self.vector[:, 0]


if __name__ == '__main__':
    path = 'Dados - Trabalho Final-20210629/att48.tsp.txt'

    graph = createGraph(path)

    print(graph.distanceBetweenVertices(1, 2))
