from tkinter import messagebox

class interpolacion_procedimiento:

    def interpolacion(funcion, x_i, x_f, iteraciones = 1000, error_relativo = 0.001):
        solucion = ""
        contador = 0
        error_calculado = 101

        if funcion(x_i) * funcion(x_f) <=0:

            while contador <= iteraciones and error_calculado >= error_relativo:
                contador += 1
                solucion = x_f - ((funcion(x_f) * (x_f - x_i))/ (funcion(x_f) - funcion(x_i)))

                error_calculado = abs((solucion - x_i) / solucion) * 100

                if funcion(x_i) * funcion(solucion) >= 0:
                    x_i = solucion
                
                else:
                    x_f = solucion
            
            print("La solucion aproximada es: {:.3f}".format(solucion))
            print("Encontrada en {:.0f}".format(contador) + "iteraciones")
            print("Con un error relativo: {:.3f}".format(error_calculado) + "%")

        else:
            print("No existe solucion en ese intervalo")


    
b = interpolacion_procedimiento()

#(lambda x: 4*x**4 -9*x**2 +1, 0, 1, 5, 5)