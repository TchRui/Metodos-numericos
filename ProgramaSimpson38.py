
import sympy as sp

class Programa_simpson_3_8:
    def Procedimiento_simpson(self,funcion,a,b):
        h = (b-a)/3
        
        x0 = a
        x1 = x0 + h
        x2 = x1 + h
        x3 = b
        
        #Primera evaluacion
        x = x0
        valor_x0 = eval(funcion)
        print("Valor de la primera integral: ",valor_x0)

        #Segunda evaluacion
        x = x1
        valor_x1 = eval(funcion)
        print("Valor de la segunda igualacion: ",valor_x1)

        #Tercera evaluacion
        x = x2
        valor_x2 = eval(funcion)
        print("Valor de la tercera igualacion: ",valor_x2)

        #Cuarta evaluacion
        x = x3
        valor_x3 = eval(funcion)
        print("Valor de la cuarta igualacion: ", valor_x3)

        #Valor real de la funcion
        x = sp.Symbol('x')
        integral = sp.integrate(funcion, (x, a, b))

        x = a
        valor_integral = integral.evalf()
        print("Valor real de la integral: ",valor_integral)

        #Regla de simpson 1/3
        simpson = ((3*h)/8)*(valor_x0+(3*valor_x1)+(3*valor_x2)+valor_x3)
        print("Valor aproximado de la integral: ",simpson)

        #Error aproximado
        error = abs((simpson-valor_integral)/simpson)*100
        print("El error aproximado: ",error)

if __name__ == "__main__":
    p = Programa_simpson_3_8()
    p.Procedimiento_simpson()
