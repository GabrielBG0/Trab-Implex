import HC
import SA

if __name__ == '__main__':
    paths = ['Dados - Trabalho Final-20210629/att48.tsp.txt',
             'Dados - Trabalho Final-20210629/berlin52.tsp.txt',
             'Dados - Trabalho Final-20210629/bier127.tsp.txt',
             'Dados - Trabalho Final-20210629/eil76.tsp.txt',
             'Dados - Trabalho Final-20210629/eil101.tsp.txt',
             'Dados - Trabalho Final-20210629/kroA100.tsp.txt',
             'Dados - Trabalho Final-20210629/kroE100.tsp.txt',
             'Dados - Trabalho Final-20210629/pr76.tsp.txt',
             'Dados - Trabalho Final-20210629/rat99.tsp.txt',
             'Dados - Trabalho Final-20210629/st70.tsp.txt']

    print('Por favor enrte com os parametros para o algoritimo Simulated Annealing')
    T = int(input('T: '))
    factor = float(input('Fator: '))

    for path in paths:
        print('-------------------------------------------------------------------------')
        print('File ' + path)
        solution, distance = SA.run(path, T, factor)
        print('SA Distance = ' + str(distance))
        solution, distance = HC.run(path)
        print('HC Distance = ' + str(distance))
    print('-------------------------------------------------------------------------')
