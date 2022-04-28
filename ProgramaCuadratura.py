from cmath import sqrt
import sympy as sp

class Programa_cuadratura_Gauss:
    def procedimiento_Cuadratura(self,funcion,a,b):
        centro = (a+b)/2

        #Calulando la mitad superior
        x1 = centro + (1/sqrt(3)) * ((b-a)/2)

        #Calculando la mitad inferior
        x0 = centro - (1/sqrt(3)) * ((b-a)/2)

        #Calculado el valor de la integral
        x = x0
        evauluacion_1 = eval(funcion)
        print("El valor de la primera funcion es: ",evauluacion_1)

        x = x1
        evauluacion_2 = eval(funcion)
        print("El valor de la segunda funcion es: ",evauluacion_2)

        valor_integral_aproximada = (evauluacion_1 + evauluacion_2)
        print("El valor aproximado de la integral es: ",valor_integral_aproximada)


if __name__ == "__main__":
    o = Programa_cuadratura_Gauss()
    o.procedimiento_Cuadratura("x",1,4)