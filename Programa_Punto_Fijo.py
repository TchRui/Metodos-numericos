import sympy as sp
from math import *

class Programa_punto_fijo:
    def Procedimiento_punto_fijo(self, funcion, x0, tolerancia, iteraciones):
        x = sp.Symbol('x')
        g = sp.lambdify(x, funcion)

        lista_resultados = []

        for i in range(iteraciones):

            x1 = g(x0)

            error = abs(x1 - x0)
            print("Error: ", error)

            if abs(x1 - x0) < tolerancia:

                cadena_resultados = "Iteracion: " + str(i) + "  |   x: "+ str(x1) + "  |   Error: " + str(error)
                lista_resultados.append(cadena_resultados)

                print("Iteracion: ", i)
                break

            x0 = x1
            cadena_resultados = "Iteracion: " + str(i) + "  |   x: "+ str(x1) + "  |   Error: " + str(error)
            lista_resultados.append(cadena_resultados)

        return lista_resultados 

if __name__ == "__main__":
    funcion = input("Ingrese la funcion f(x): ")
    programa = Programa_punto_fijo()
    resultados = programa.Procedimiento_punto_fijo(funcion, 0.5, 0.00000001, 50)
    for i in resultados:
        print(i)

    #(っ◔◡◔)っ ❤