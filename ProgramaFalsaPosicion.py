from argon2 import PasswordHasher
import sympy as sp
from math import *


#Requerimientos para el problema de la falsa posicion
#Definir xl y xu

class Programa_falsa_posicion:
    def Procedimiento_falsa_posicion(self,funcion,xl,xu,tolerancia,iteraciones):
        
        lista_resultados = []

        for i in range(iteraciones):
            #Evaluar la funcion en xl
            x = xl
            fxl = eval(funcion)

            #Evaluamos la funcion en terminos de xu
            x = xu
            fxu = eval(funcion)

            #Realizamos la evaluacion del punto fijo
            xr = (xu)*((fxu)*(xl-xu)/(fxl-fxu))

            #Evaluamos en terminos de xr
            x = xr
            fxr = eval(funcion)

            #Realizamos la multiplicacion
            multiplicacion = fxl * fxr

            if multiplicacion > 0:
                error = (xu-xl)/xu
                cadena_resultado = "Iteracion: " + str(i) + "   | Xl: " + str(xl) + "   | Xu: " + str(xu) + "   | Error: " + str(error)
                lista_resultados.append(cadena_resultado)
                xl = xr

                if error < tolerancia:
                    break


            elif multiplicacion < 0:
                error = (xu-xl)/xu
                cadena_resultado = "Iteracion: " + str(i) + "   | Xl: " + str(xl) + "   | Xu: " + str(xu) + "   | Error: " + str(error)
                lista_resultados.append(cadena_resultado)
                xu = xr

                if error < tolerancia:
                    break
            
            elif multiplicacion == 0:
                error = (xu-xl)/xu
                cadena_resultado = "Iteracion: " + str(i) + "   | Xl: " + str(xl) + "   | Xu: " + str(xu) + "   | Error: " + str(error)
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
    
    programa = Programa_falsa_posicion()
    programa.Procedimiento_falsa_posicion(funcion,xl,xu,tolerancia,iteraciones)