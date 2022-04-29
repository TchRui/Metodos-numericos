import sympy as sp

class Programa_3_puntos:
    def procedimiento_3_puntos(self, funcion, x, h):
        x0 = x
        
        #Evaluacion de la funcion en x - h
        x = x0 - h
        valor_a = eval(funcion)
        print("El valor de la funcion en x - h",valor_a)

        #Evaluacion de la funcion en x + h
        x = x0 + h
        valor_b = eval(funcion)
        print("El valor de la funcion en x + h",valor_b)

        #derifada final
        derivada_f = (1/(2*h))*(valor_a + valor_b)
        print("Valor de la derivada aproximada: ",derivada_f)

        #Aquí se obtiene el valor real de la derivada
        x = sp.Symbol('x')
        derivada_real = sp.diff(funcion, x)

        x = x0
        valor_derivada_real = eval(str(derivada_real))
        print("Valor real de la derivada: ",valor_derivada_real)

if __name__ == "__main__":
    Programa_3_puntos().procedimiento_3_puntos("x**3",0,1)