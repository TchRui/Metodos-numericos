
import numpy as np
import matplotlib.pyplot as plt 
import sympy as sp

class Programa_Punto_Fijo:

    def procedimiento_punto_fijo(self,f1,f2,f1desp,f2desp,x,y,iteraciones):
        
        def fdespejada(vector):
            x = self.valorx
            y = self.valory
            evalf1desp = eval(f1desp)
            evalf2desp = eval(f2desp)
            return np.array([evalf1desp,evalf2desp])

        lista = []

        vector = np.array([x,y])
           
        for i in range(int(iteraciones)):
            vectorold = vector
            e = np.linalg.norm(vector - vectorold)
            self.x = vector[0]
            self.y = vector[1]

            if abs(e < 0.0):
                cadena_resultado = "x" + str(i) + " = " + str(x) + " y" + str(i) + " = " + str(y), "Error = " + str(e)
                lista.append(cadena_resultado)
                return lista
            
            
            cadena_resultado = "x" + str(i) + " = " + str(x) + " y" + str(i) + " = " + str(y), "Error = " + str(e)
            lista.append(cadena_resultado)
        
