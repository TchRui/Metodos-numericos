import sympy as sp
from tkinter import messagebox
class Programa_trapecio:
    def Procedimiento_trapecio(self,función,a,b):
        #Limite inferior
        x = a
        valor_a = eval(función)
        print(valor_a)

        #Limite superior
        x = b
        valor_b = eval(función)
        print(valor_b)

        resultado = ((valor_a + valor_b) / 2) * (b - a)

        x = sp.Symbol('x')
        integral = sp.integrate(función, (x, a, b))

        x = a
        valor_integral = integral.evalf()
        print("Valor real de la integral: ",valor_integral)

        print("Valor aproximado: ",resultado)

        error_aprox = abs((valor_integral - resultado)/valor_integral)*100

        lista_resultado = []

        cadena_resultado = "Valor aproximado: " + str(resultado)  + "   |   Valor real de la integral: " + str(valor_integral) + "   |   Error: " + str(error_aprox) + "%"
        lista_resultado.append(cadena_resultado)

        return lista_resultado
        


if __name__ == "__main__":
    Programa_trapecio().Procedimiento_trapecio()