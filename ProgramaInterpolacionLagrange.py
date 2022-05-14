import sympy as sp
from tkinter import messagebox

class Programa_Interpolacion_Lagrange:
    def procedimiento_lagrange(self,valores):
        if len(valores) == 3:
            x0 = valores[0][0]
            fx0 = valores[0][1]

            x1 = valores[1][0]
            fx1 = valores[1][1]

            x2 = valores[2][0]
            fx2 = valores[2][1]

            x = sp.Symbol('x')

            #Obteniendo el primer polinomio
            a1= (x - x1)
            a2 = (x - x2)
            a = (a1*a2)
            a_expandida = sp.expand(a)

            b1 = (x0 - x1)
            b2 = (x0 - x2)
            b = (b1*b2)

            l0x = a_expandida / b
            #print("El polinomio interpolante lx0 es: " + str(l0x))


            #Obteniendo el segundo polinomio
            temporal_1 = (x - x0)
            temporal_2 = (x - x2)
            polinomio_numerador_2 = (temporal_1*temporal_2)
            polinomio_numerador_2_expandido = sp.expand(polinomio_numerador_2)            

            temporal_denominador_1 = (x1 - x0)
            temporal_denominador_2 = (x1 - x2)
            polinomio_denominador_2 = (temporal_denominador_1*temporal_denominador_2)
            polinomio_denominador_2_expandido = sp.expand(polinomio_denominador_2)

            l1x = polinomio_numerador_2_expandido / polinomio_denominador_2_expandido
            #print("El polinomio interpolante lx1 es: " + str(l1x))
            
            #obteniendo el tercer polinomio
            temporal_numerador_3 = (x - x0)
            temporal_numerador_4 = (x - x1)
            polinomio_numerador_3 = (temporal_numerador_3*temporal_numerador_4)
            polinomio_numerador_3_expandido = sp.expand(polinomio_numerador_3)

            temporal_denominador_3 = (x2 - x0)
            temporal_denominador_4 = (x2 - x1)
            polinomio_denominador_3 = (temporal_denominador_3*temporal_denominador_4)
            polinomio_denominador_3_expandido = sp.expand(polinomio_denominador_3)

            l2x = polinomio_numerador_3_expandido / polinomio_denominador_3_expandido
            #print("El polinomio interpolante lx2 es: ", l2x)

            #Obteniendo el polinomio interpolante
            polinomio_interpolante = (fx0*l0x) + (fx1*l1x) + (fx2*l2x)
            #print("El polinomio interpolante es: ", polinomio_interpolante)

            messagebox.showinfo("Interpolacion de Lagrange", "El polinomio interpolante es: " + str(polinomio_interpolante))

    
if __name__ == "__main__":
    valores = [[0,1],[1,3],[2,0]]
    programa = Programa_Interpolacion_Lagrange()
    programa.procedimiento_lagrange(valores)

