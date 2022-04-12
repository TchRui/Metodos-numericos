import sympy as sp

class Programa_Taylor:
    def Procedimiento_Taylor(self, funcion, x_valor, h):

        def funcion_derivada(funcion, x_valor, h):
            x = sp.Symbol('x')
            funcion_derivada = sp.diff(funcion, x)
            print(eval(str(funcion_derivada)(x_valor)))
        
        def funcion_x(x_valor):
            x = x_valor
            return eval(funcion)
        
        def funcion_x1():
            x = x_valor
            return eval(funcion)
        

