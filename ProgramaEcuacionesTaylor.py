import sympy as sp
from math import *
from tkinter import messagebox
class Programa_Ecuaciones_Taylor:
    def Procedimiento_Ecuaciones_Taylor(self,f,n,h):
        x = sp.Symbol('x')
        if n == 1:
            #Encontrar la primera derivada
            primera_derivada = sp.diff(f,x)

            #Evaluar la ecuación de taylor
            taylor = (primera_derivada / factorial(2))*(h**2)
            messagebox.showinfo("Taylor","El resultado de la evaluación es: " + str(taylor))
    
        elif n == 2:
            #Encontrar la primera derivada
            primera_derivada = sp.diff(f,x)

            #Encontrar la sengunda derivada
            segunda_derivada = sp.diff(primera_derivada,x)

            #Evaluar la ecuación de taylor
            taylor = ((primera_derivada / factorial(2))*(h**2)) + ((segunda_derivada / factorial(3))*(h**3))
            messagebox.showinfo("Taylor","El resultado de la evaluación es: " + str(taylor))
        
        elif n == 3:
            #Encontrar la primera derivada
            primera_derivada = sp.diff(f,x)

            #Encontrar la sengunda derivada
            segunda_derivada = sp.diff(primera_derivada,x)

            #Encontrar la tercera derivada
            tercera_derivada = sp.diff(segunda_derivada,x)     

            #Evaluar la ecuación de taylor
            taylor = ((primera_derivada / factorial(2))*(h**2)) + ((segunda_derivada / factorial(3))*(h**3)) + ((tercera_derivada / factorial(4))*(h**4))
            messagebox.showinfo("Taylor","El resultado de la evaluación es: " + str(taylor))   


if __name__ == "__main__":
    p = Programa_Ecuaciones_Taylor()
    p.Procedimiento_Ecuaciones_Taylor()