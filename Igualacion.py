from sympy import *
from tkinter import messagebox
class igualacion:

    def procedimiento_igualacion(self,a,b,c,d,e,f,):
        x = Symbol('x')
        y = Symbol('y')

        resultado = solve([a*x+b*y+c,d*x+e*y+f],[x,y])
        print(resultado)
        
        messagebox.showinfo("Aviso", "Los valores quedan de la siguiente manera: " + str(resultado))

objeto = igualacion()
