import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np

class Programa_Jacobi:
    def procedimiento_jacobi(self,n,A,B,tool,error,nitermax):
        lista = []

        alpha = 3 * n
        ADD = np.dot(A,A.T) + alpha*np.identity(n)
        A = ADD
        determ = np.linalg.det(A)
        print(determ)
        n = len(B)
        count = 0
        for i in range(n):
            Aii = A[i][i]
            suma = 0
            for j in range(n):
                if i != j:
                    suma = suma + abs(A[i][j])
            if Aii > suma:
                print("La fila", i, "es dominante")
                count = count + 1
            else:
                print("La fila", i, "no es dominante")
                break
        if count == n:
            print("La matriz es diagonal dominante y el metodo iterativo converge")
        else:
            print("La matriz no es diagonal dominante y el metodo iterativo no converge")

        #Valores iniciales
        n = len(A)
        x = np.zeros(n)
        x1 = np.zeros(n)
        niter = 0
        Niter = []
        Error = []

        while niter < nitermax and error > tool:
            for i in range(n):
                d = B[i]
                for j in range(n):
                    if i != j:
                        d = d - A[i][j]*x[j]

                x[i] = d/A[i][i]
            error = np.linalg.norm(x-x1)
            x1 = np.copy(x)

            cadena_resultados = "Iteracion: " + str(niter) + "  |   x: "+ str(x) + "  |   Error: " + str(error/np.linalg.norm(B))
            lista.append(cadena_resultados)

            print("Iteracion: ", niter)
            print("x: ", x)
            print("Error en la iteracion: ", niter, "es: ", error/np.linalg.norm(B))
            niter += 1
            Niter.append(niter)
            Error.append(error)

        x = Niter
        y = Error

        plt.plot(x, y,label="Variacion del error")
        plt.plot()

        plt.xlabel('Iteraciones')
        plt.ylabel('Error')
        plt.title('Metodo de Jacobi')
        plt.legend()
        plt.grid()
        plt.show()
        return lista

        