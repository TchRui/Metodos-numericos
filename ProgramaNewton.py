import numpy as np
import sympy as sp

class Programa_Newton:
    def procedimiento_newton(self,f1,f2,x,y,iteraciones):
        
        def F(vector):
            x = vector[0]
            y = vector[1]
            valf1 = eval(f1)
            valf2 = eval(f2)
            vector = np.array([valf1,valf2])
            return vector

        def dF(vector):
            x1,y1,z,w,sin,cos,tan,cot,sec,csc,asin,acos,atan,acot,asec,acsc = sp.symbols('x y z w sin cos tan cot sec csc asin acos atan acot asec acsc')
            deriv1x = sp.diff(f1,x1)
            deriv1y = sp.diff(f1,y1)
            deriv2x = sp.diff(f2,x1)
            deriv2y = sp.diff(f2,y1)

            x = self.valorx
            y = self.valory

            dx1 = eval(str(deriv1x))
            dy1 = eval(str(deriv1y))
            dx2 = eval(str(deriv2x))
            dy2 = eval(str(deriv2y))

            vector = np.array([[dx1,dy1],[dx2,dy2]])

            return vector
                            
        N = int(iteraciones) + 1
        vector = np.array([x,y])

        lista_resultados = [""]

        for k in range(N):
            vectorold = vector
            self.valorx = vector[0]
            self.valory = vector[1]

            Jinv = np.linalg.inv(dF(vector))

            vector = vector - np.dot(Jinv,F(vector))

            e = np.linalg.norm(vector - vectorold)

            cadena_resultados = ("Iteracion: " + str(k) + " |   Resultado: " + str(vector) + "    |   Error: " + str(e))
            lista_resultados.append(cadena_resultados)
            
            if e <= 0.0:
                break
        
        return lista_resultados