import sympy as sp
from math import *
from tkinter import messagebox
from threading import *

class Programa_Euler:
    def Procedimiento_Euler(self, f, xi, xe, yi, n):
        x, y, = sp.symbols('x y')
        
        #Calcular la primera formulam delta x
        delta_x = (xe - xi)/n

        lista_valores_x = []

        for i in range(n):
            xn = xi + (i*delta_x)
            lista_valores_x.append(xn)
        
        lista_resultados_iteraciones = []

        for i in range(n + 1):
            if i == 0:
                y = yi
                x = lista_valores_x[0]
                funcion_evaluada = eval(f)
                lista_temporal = [0,lista_valores_x[0],yi,funcion_evaluada]
                lista_resultados_iteraciones.append(lista_temporal)
                lista_temporal = []
            
            elif i < n and i > 0:
                valorf = lista_resultados_iteraciones[i-1][3]
                valory = lista_resultados_iteraciones[i-1][2]
                y = valory + (delta_x*valorf)
                x = lista_valores_x[i]                
                funcion_evaluada = eval(f)
                lista_temporal = [i,x,y,funcion_evaluada]
                lista_resultados_iteraciones.append(lista_temporal)
                lista_temporal = []

        #Ultima iteracion de la tabla para obtener el valor resultante
        valorf = lista_resultados_iteraciones[-1][3]
        valory = lista_resultados_iteraciones[-1][2]
        y = valory + (delta_x*valorf)
        x = x + delta_x
        lista_temporal = [i,x,y,""]
        lista_resultados_iteraciones.append(lista_temporal)
                       
        lista_retorno = []
        
        for i in range(n + 1):
            i = lista_resultados_iteraciones[i][0]
            x = lista_resultados_iteraciones[i][1]
            y = lista_resultados_iteraciones[i][2]
            f = lista_resultados_iteraciones[i][3]
            cadena_resultados = "Iteracion: " + str(i) + "  | Valor de x: "+ str(x) + " |Valor de y:" + str(y) + "  | Valor de la funcion: " + str(f)
            lista_retorno.append(cadena_resultados)
        
        
        return lista_retorno
if __name__ == "__main__":
    p = Programa_Euler()
    p.Procedimiento_Euler("0.1*sqrt(y)+0.4*x**2",2, 2.5, 4,10)