import sympy as sp
from math import *

class Programa_biseccion:
    def Procedimiento_biseccion(self, funcion, xl, xu, tolerancia, iteraciones):

        lista_resultados = []

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
            fm = eval(funcion)
            
            #Condiciones de paro
            if (fa * fm) < 0:
                error = (xl + xu) /2
                cadena_resultado = "Iteracion: " + str(i) + "  Xl: " + str(xl) + "  Xu: " + str(xu) + "  Error: " + str(error)
                lista_resultados.append(cadena_resultado)
                xu = m
                
                if error < tolerancia:
                    break


            elif (fa * fm) > 0:
                error = (xl + xu) /2
                cadena_resultado = "Iteracion: " + str(i) + "  Xl: " + str(xl) + "  Xu: " + str(xu) + "  Error: " + str(error)
                lista_resultados.append(cadena_resultado)
                xl = m

                if error < tolerancia:
                    break
                
            else:
                error = (xl + xu) /2
                cadena_resultado = "Iteracion: " + str(i) + "  Xl: " + str(xl) + "  Xu: " + str(xu) + "  Error: " + str(error)
                lista_resultados.append(cadena_resultado)
                break
            
        for i in lista_resultados:
            print(i)

            
        

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