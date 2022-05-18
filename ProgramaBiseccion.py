import sympy as sp
from math import *

class Programa_biseccion:
    def Procedimiento_biseccion(self, funcion, xl, xu, tolerancia, iteraciones):

        for i in range(iteraciones):
            m = (xl + xu) /2
            
            #Evaluacion de F en a
            x = xl
            fa = eval(funcion)

            #Evaluacion de F en b
            x = xu
            fb = eval(funcion)

            #Evaluacion de F en m 

            x = m
            fb = eval(funcion)
            
        

if __name__ == "__main__":
    funcion = '(e**3*x)-4'
    xl = 0
    xu = 1
    tolerancia = 0.01
    iteraciones = 10000

    programa = Programa_biseccion()
    resultados = programa.Procedimiento_biseccion(funcion, xl, xu, tolerancia, iteraciones)

    for i in resultados:
        print(i)