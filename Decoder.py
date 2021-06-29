import numpy as np


def generateVector(path):
    vector = np.loadtxt(path, dtype=int, delimiter=' ')
    return vector


class Graph:
    def __init__(self, vector):
        self.vector = vector

    def distanceBetweenVertices(self, v1, v2):
        # TODO calcula a distancia entre dois vertices
        return

    def getVerticeCoords(self, v):
        # TODO retorna coordenadas de um vertice
        return
