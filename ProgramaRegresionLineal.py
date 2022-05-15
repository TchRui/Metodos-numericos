from cProfile import label
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class Programa_regresion_lineal:
    def procedimiento_regresion(self, lista_x, lista_y):
        x = np.array(lista_x)
        y = np.array(lista_y)

        suma_x = np.sum(x)
        suma_y = np.sum(y)

        suma_x2 = np.sum(x**2)
        suma_y2 = np.sum(y**2)
        suma_xy = np.sum(x*y)

        promedio_x = suma_x/len(x)
        promedio_y = suma_y/len(y)

        n = len(x)

        m = ((suma_x*suma_y) - (n*suma_xy))/((suma_x**2)-(n*suma_x2))
        b = promedio_y - (m*promedio_x)

        sigma_x = np.sqrt((suma_x2/n) - (promedio_x**2))
        sigma_y = np.sqrt((suma_y2/n) - (promedio_y**2))
        sigma_xy = suma_xy/n - promedio_x*promedio_y
        regresion_cuadrada = (sigma_xy/(sigma_x*sigma_y))**2

        plt.plot(x, y, 'o', label='Datos')
        plt.plot(x, m*x + b, 'r', label='Regresion')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Regresion lineal')
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    lista_x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    lista_y = [1,2,2,4,5,4,6,4,6,7,9,10,11,12,10]
    programa = Programa_regresion_lineal()
    programa.procedimiento_regresion(lista_x, lista_y)