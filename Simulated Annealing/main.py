import numpy
import matplotlib.pyplot as plt


class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distancia(a, b):
        return numpy.sqrt(numpy.abs(a.x - b.x) + numpy.abs(a.y - b.y))

    @staticmethod
    def get_total(coord):
        dist = 0
        for primeiro, segundo in zip(coord[:-1], coord[1:]):
            dist += Coordenada.get_distancia(primeiro, segundo)
        dist += Coordenada.get_distancia(coord[0], coord[-1])
        return dist


if __name__ == '__main__':
    coord = []
    for i in range(20):
        coord.append(Coordenada(
            numpy.random.uniform(), numpy.random.uniform()))

        fig = plt.figure(figsize=(10, 5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        for primeiro, segundo in zip(coord[:-1], coord[1:]):
            ax1.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
        ax1.plot([coord[0].x, coord[-1].x], [coord[0].y, coord[-1].y], 'b')
        for c in coord:
            ax1.plot(c.y, c.y, 'ro')

    # SIMULATED ANNAELING
    custo0 = Coordenada.get_total(coord)

    T = 30
    factor = 0.99
    T_init = T
    for i in range(1000):
        print(i, 'custo = ', custo0)

        T = T * factor
        for j in range(500):
            # TROCA DUAS COORDENADAS E PEGA A SOLUÇÃO VIZINHA
            r1, r2 = numpy.random.randint(0, len(coord), size=2)

            temp = coord[r1]
            coord[r1] = coord[r2]
            coord[r2] = temp

    # GET NOVO CUSTO
    custo1 = Coordenada.get_total(coord)

    if custo1 < custo0:
        custo0 = custo1
    else:
        x = numpy.random.uniform()
        if x < numpy.exp((custo0 - custo1) / T):
            custo0 = custo1
        else:
            temp = coord[r1]
            coord[r1] = coord[r2]
            coord[r2] = temp

    # RESULTADO
    for primeiro, segundo in zip(coord[:-1], coord[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([coord[0].x, coord[-1].x], [coord[0].y, coord[-1].y], 'b')
    for c in coord:
        ax2.plot(c.y, c.y, 'ro')

    plt.show()
