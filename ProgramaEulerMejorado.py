import sympy as sp
from math import *

from tkinter import messagebox

class Programa_Euler_Mejorado:
    def Procedimiento_Euler(self,f,h,x0,y0,xf):
        xn = x0
        yn = y0

        x = x0
        y = y0
        evaulacion1 = eval(f)
        yn1 = y0 + h*evaulacion1

        #Calculamos los valores de xn+1 que es xn + h
        xn1 = xn + h

        #Calculamos los valores de yn+1 que es yn + (h/2)*(f(xn,yn)+f(xn+h,yn+h))
        x = xn1
        y = yn1
        evaulacion2 = eval(f)
        yn1ext = yn + (h/2)*(evaulacion1 + evaulacion2)

        #Asignamos los nuevos valores a las variables x0 y y0
        x0 = xn
        y0 = yn1ext
        x0 = round(x0,2)
        y0 = round(y0,2)

        #Imprimimos los valores de xn, yn, xn+1 y yn+1
        #print("xn = ",xn," yn = ",yn,"yn+1 = ",yn1," xn+1 = ",xn1," yn+1 = ",yn1ext)
        flag = True

        while flag:
            #Obtenemos el valor de xn el cual es la suma de x0 y h
            xn = x0 + h
            yn = y0

            xn = round(xn,2)
            yn = round(yn,2)

            #Obtener el valor de yn el cual es la suma de y0 y h*f(x0,y0)
            x = xn
            y = yn
            evaulacion1 = eval(f)
            yn1 = y0 + h*evaulacion1

            #Calculamos los valores de xn+1 que es xn + h
            xn1 = xn + h
            xn1 = round(xn1,2)

            #Calculamos los valores de yn+1 que es yn + (h/2)*(f(xn,yn)+f(xn+h,yn+h))
            x = xn1
            y = yn1
            evaulacion2 = eval(f)
            yn1ext = yn + (h/2)*(evaulacion1 + evaulacion2)

            #Asignamos los nuevos valores a las variables x0 y y0
            x0 = xn
            y0 = yn1ext

            #Imprimimos los valores de xn, yn, xn+1 y yn+1
            #print("xn = ",xn," yn = ",yn,"yn+1 = ",yn1," xn+1 = ",xn1," yn+1 = ",yn1ext)

            #Condicion para que el programa se detenga
            if xn1 > xf:
                flag = False
        
        messagebox.showinfo("Resultado","El valor resultante es: " + str(yn))
            
if __name__ == "__main__":
    p = Programa_Euler_Mejorado()
    p.Procedimiento_Euler("2*x*y",0.1,1,1,1.5)