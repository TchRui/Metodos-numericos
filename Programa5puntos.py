import sympy as sp

class Programa_5_puntos:
    def procedimiento_5_puntos(self,funcion, x, h):
        x0 = x
        e = sp.Symbol('exp')
        #Evaluacion de la funcion en x0
        x = x0 + h
        print("El valor de x0 es: ", x0)
        valor_x0 = eval(funcion)
        print("El valor de la funcion en x0: ",valor_x0)

        #Evaluacion de la funcion en x1
        x = x0 - h

        valor_x1 = eval(funcion)
        print("El valor de la funcion en x1: ",valor_x1)
        
        #Evaluacion de la funcion en x2
        x = x0 + 2*h
        valor_x2 = eval(funcion)
        print("El valor de la funcion en x2: ",valor_x2)

        #Evaluacion de la funcion en x3
        x = x0 - 2*h
        valor_x3 = eval(funcion)
        print("El valor de la funcion en x3: ",valor_x3)

        #Formula de los 5 puntos
        derivada_f = (1/12*h)(valor_x3 - 8*valor_x1 + 8*valor_x0 - valor_x2)
        print("El valor de la derivada aproximada es :", derivada_f)

if __name__ == "__main__":
    programa = Programa_5_puntos()
    programa.procedimiento_5_puntos()