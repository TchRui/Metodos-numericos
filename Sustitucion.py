import numpy as np
from tkinter import messagebox

class sustitucion:
    def procedimiento_sustitucion(self,a,b,c,d,e,f):
        a = np.array([[a,b],[d,e]])
        b= np.array([c,f])
        resultado = np.linalg.solve(a,b)
        print("x: ", resultado[0])
        print("y: ", resultado[1])
        messagebox.showinfo("Aviso", "Los valores de x es: " + str(resultado[0]) + " y de y: " + str(resultado[1]))

s = sustitucion()
