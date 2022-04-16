
import sympy as sp

class Programa_simpson_1_3:
    def Procedimiento_simpson(self,funcion,a,b):
        h = (b-a)/2

        x0 = a
        x1 = x0 + h
        x2 = b
        print("Valor de x0: ", x0)
        print("Valor de x1: ", x1)
        print("Valor de x2: ", x2)

        #Primera evaluacion
        x = x0
        valor_x0 = eval(funcion)
        print("Valor de la primera integral: ",valor_x0)

        #Segunda evaluacion
        x = x1
        valor_x1 = eval(funcion)
        print("Valor de la segunda igualacion: ",valor_x1)

        #Tercera igualacion
        x = x2
        valor_x2 = eval(funcion)
        print("Valor de la tercera igualacion: ",valor_x2)

        #Valor real de la funcion
        x = sp.Symbol('x')
        integral = sp.integrate(funcion, (x, a, b))

        x = a
        valor_integral = integral.evalf()
        print("Valor real de la integral: ",valor_integral)

        #Regla de simpson 1/3
        simpson = (h/3)*(valor_x0+(4*valor_x1)+valor_x2)
        print("Valor aproximado de la integral: ",simpson)

        #Error aproximado
        error = abs((simpson-valor_integral)/simpson)*100
        print("El error aproximado: ",error)

        lista_resultado = []
        cadena_resultado = "Valor aproximado: " + str(simpson)  + "   |   Valor real de la integral: " + str(valor_integral) + "   |   Error: " + str(error) + "%"
        lista_resultado.append(cadena_resultado)

        return lista_resultado

if __name__ == "__main__":
    p = Programa_simpson_1_3()
    p.Procedimiento_simpson()

