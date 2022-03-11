from tkinter import messagebox
import numpy as np


class procedimiento:
    def procedimiento_reduccion(self, a, b, c, d, e, f):

        ecu_1 = np.array([[a,b],[d,e]])
        ecu_2 = np.array([c, f])
        resultado = np.linalg.solve(ecu_1, ecu_2)

        a_temp = a

        temp_a = a
        temp_b = b
        temp_c = c

        a = a * d
        b = b * d
        c = c * d

        d = d * a_temp * -1
        e = e * a_temp * -1
        f = f * a_temp * -1

        y = b + e
        w = c + f

        if y > 1:
            y_despejada = (w / y) 

        elif y == 1:
            y_despejada = w
        
        elif y < 0:
            y_despejada = (w / y) * -1

        if y < 0:
            y_despejada = y_despejada * -1
        
        if temp_a > 1 or temp_a < 0:
            b_despejada = (temp_b * y_despejada)
            
            if b_despejada > 0:
                temp_c = temp_c - b_despejada
            else:
                temp_c = temp_c - b_despejada
            
            x_despejada = temp_c / temp_a
        
        elif temp_a == 1:
            b_despejada = (temp_b * y_despejada)
            
            if b_despejada > 0:
                temp_c = temp_c - b_despejada
            else:
                temp_c = temp_c + b_despejada
            
            x_despejada = temp_c

        flag = False 

        messagebox.showinfo("Sucess", "El valor para x es de: " + str(x_despejada) + " y de y es de: " + str(y_despejada))   
        return True
pr = procedimiento()