import sympy as sp

class Programa_Taylor:
    def Procedimiento_Taylor(self, funcion, x_valor, h, decremento, tolerancia):
        x = sp.Symbol('x')
        #Derivamos la funcion en terminos de x
        funcion_derivada = sp.diff(funcion, x)
        
        x = x_valor
        valor_real = eval(str(funcion_derivada))
        #print("f'(x) = ", valor_real)
        
        #Primera funcion
        def funcion_x(x_valor):
            x = x_valor
            return eval(funcion)

        #Segunda funcion
        def funcion_x1(xi):
            x = xi
            return eval(funcion)

        #Ciclo para realizar las iteraciones
        flag = False
        lista_resultados = []
        contador = 0
        while not flag:
            contador += 1

            resultado_fx = funcion_x(x)
            #print("f(x) = ", resultado_fx)

            xi = x + h

            resultado_fx1 = funcion_x1(xi)
            #print("f(x+h) = ", resultado_fx1)

            valor_taylor = (resultado_fx1 - resultado_fx) / h
            #print("Taylor = ", valor_taylor)

            error = abs(valor_real - valor_taylor)*100
            #print("Error = ", error)
            
            h = h - decremento
            #print("h = ", h)
            
            cadena_resultados = "Iteracion: " + str(contador) + "   | Valor aproximado: " + str(valor_taylor) + "   | Error: " + str(error)+" %"
            lista_resultados.append(cadena_resultados)
            
            if (error/100) < tolerancia:
                flag = True
                break
        
        for i in lista_resultados:
            print(i)
        
        #Retorno la lista que contiene todos los resultados de las iteraciones
        return lista_resultados

            

if __name__ == "__main__":
    Programa_Taylor().Procedimiento_Taylor("-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2",0.5,0.25,0.01,0.01)