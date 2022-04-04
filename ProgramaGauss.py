class Programa_Gauss_Seiel:
    def SOR(self,A,B,x,imax,es,omega,tool):
        ea = 0
        lista = []
        lista_Errores = []

        n = len(x)
        for i in range(n):
            dummy = A[i][i]
            for j in range(n):
                A[i][j] = A[i][j]/dummy
            B[i] = B[i]/dummy

            for i in range(n):
                sum = B[i]
                for j in range(n):
                    if i != j:
                        sum = sum - A[i][j]*x[j]
                x[i] = sum
        iter = 1

        while iter <= imax or ea > tool:
            centinela = 1
            for i in range(n):
                old = x[i]
                sum = B[i]
                for j in range(n):
                    if i != j:
                        sum -= A[i][j]*x[j]
                x[i] = omega*sum + (1-omega)*old

                if centinela == 1 and x[i] != 0:
                    ea = abs((x[i] - old)/x[i])*100
                    lista_Errores.append(ea)
                    if ea > tool:
                        centinela = 0
                
                cadena_resultados = "Iteracion: " + str(iter) + "  |   valores x,y,z: "+ str(x) + "  |   Error: " + str(ea)
                lista.append(cadena_resultados)
                iter += 1
                if centinela == 1 or iter > imax or ea >= tool:
                    break
        return x,lista

