import sympy as sp
from tkinter import messagebox

class Programa_Interpolacion_Newton:
    def procedimiento_newton(self, valores):
        if len(valores) == 2:
            x0 = valores[0][0]
            fx0 = valores[0][1]

            x1 = valores[1][0]
            fx1 = valores[1][1]

            fx0_x1 = (fx1 - fx0)/(x1 - x0)
        
            a0 = fx0
            a1 = fx0_x1

            x = sp.Symbol('x')
            polinomio = a0+a1*(x-x0)
            polinomio_completo = sp.expand(polinomio)
            print(polinomio_completo)

            messagebox.showinfo("Interpolacion de Newton","El polinomio interpolante es: " + str(polinomio_completo))


        elif len(valores) == 3:
            x0 = valores[0][0]
            fx0 = valores[0][1]

            x1 = valores[1][0]
            fx1 = valores[1][1]

            x2 = valores[2][0]
            fx2 = valores[2][1]

            fx0_x1 = (fx1 - fx0)/(x1 - x0)
            fx1_x2 = (fx2 - fx1)/(x2 - x1)
            fx0_x1_x2 = (fx1_x2 - fx0_x1)/(x2 - x0)

            a0 = fx0
            a1 = fx0_x1
            a2 = fx0_x1_x2

            x = sp.Symbol('x')
            polinomio = a0+a1*(x-x0)+a2*(x-x0)*(x-x1)
            polinomio_completo = sp.expand(polinomio)
            print(polinomio_completo)

            messagebox.showinfo("Interpolacion de Newton", "El polinomio interpolante es: " + str(polinomio_completo))
            
        elif len(valores) == 4:
            x0 = valores[0][0]
            fx0 = valores[0][1]

            x1 = valores[1][0]
            fx1 = valores[1][1]

            x2 = valores[2][0]
            fx2 = valores[2][1]

            x3 = valores[3][0]
            fx3 = valores[3][1]

            fx0_x1 = (fx1 - fx0)/(x1 - x0)
            fx1_x2 = (fx2 - fx1)/(x2 - x1)
            fx2_x3 = (fx3 - fx2)/(x3 - x2)
            fx0_x1_x2 = (fx1_x2 - fx0_x1)/(x2 - x0)
            fx1_x2_x3 = (fx2_x3 - fx1_x2)/(x3 - x1)

            a0 = fx0
            a1 = fx0_x1
            a2 = fx0_x1_x2
            a3 = fx1_x2_x3

            x = sp.Symbol('x')
            polinomio = a0+a1*(x-x0)+ a2*(x-x0)*(x-x1) + a3*(x-x0)*(x-x1)*(x-x2)
            polinomio_completo = sp.expand(polinomio)
            print(polinomio_completo)

            messagebox.showinfo("Interpolacion de Newton", "El polinomio interpolante es: " + str(polinomio_completo))
        
if __name__ == "__main__":
    p = Programa_Interpolacion_Newton()
    lista = [[1,2],[0,4],[-3,-2],[-1,-5]]
    p.procedimiento_newton(lista)