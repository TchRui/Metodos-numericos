from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb

from math import *
from Programa_Punto_Fijo import Programa_punto_fijo
from GUI_Resultados import Resultados

class entorno_punto_fijo:
    def principal_punto_fijo(self):
        punto_fijo_window = Tk()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = punto_fijo_window.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = punto_fijo_window.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        punto_fijo_window.geometry(posicion)

        punto_fijo_window.title('Estructura de datos - Unidad 2')
        punto_fijo_window.config(bg='#7FADA9')
        punto_fijo_window.resizable(0, 0)

        lblTitulo = Label(punto_fijo_window, text="Unidad 2: Método del punto fijo", bg="#CCD9CE", font="Times", width="28", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=4, padx=55, pady=15)

        lblFuncion = Label(punto_fijo_window, text="Función:", bg="#CCD9CE", font="Times", width="8", height="1")
        lblFuncion.grid(row=1, column=0, padx=55, pady=15)

        cajafuncion = Variable()
        cajafuncion = Entry(punto_fijo_window, width=10, font="Times", justify="center", textvariable=cajafuncion)
        cajafuncion.grid(row=1, column=1, padx=20, pady=15)

        lblX0 = Label(punto_fijo_window, text="X0:", bg="#CCD9CE", font="Times", width="8", height="1")
        lblX0.grid(row=2, column=0, padx=55, pady=15)

        cajaX0 = Variable()
        cajaX0 = Entry(punto_fijo_window, width=10, font="Times", justify="center", textvariable=cajaX0)
        cajaX0.grid(row=2, column=1, padx=20, pady=15)

        lblTolerancia = Label(punto_fijo_window, text="Tolerancia:", bg="#CCD9CE", font="Times", width="8", height="1")
        lblTolerancia.grid(row=3, column=0, padx=55, pady=15)

        cajaTolerancia = Variable()
        cajaTolerancia = Entry(punto_fijo_window, width=10, font="Times", justify="center", textvariable=cajaTolerancia)
        cajaTolerancia.grid(row=3, column=1, padx=20, pady=15)

        lblIteraciones = Label(punto_fijo_window, text="Iteraciones:", bg="#CCD9CE", font="Times", width="8", height="1")
        lblIteraciones.grid(row=4, column=0, padx=55, pady=15)

        cajaIteraciones = Variable()
        cajaIteraciones = Entry(punto_fijo_window, width=10, font="Times", justify="center", textvariable=cajaIteraciones)
        cajaIteraciones.grid(row=4, column=1, padx=20, pady=15)

        def opciones():
            if cajafuncion.get() == "":
                msb.showerror("Error", "Ingrese una función valida para continuar")
            
            try:
                if float(cajaX0.get()) == 0:
                    msb.showerror("Error", "Ingrese un valor diferente de 0 para continuar")
            except:
                msb.showerror("Error", "Ingrese un valor numerico para continuar")
            
            try:
                if float(cajaTolerancia.get()) == 0:
                    msb.showerror("Error", "Ingrese un valor diferente de 0 para continuar")
            except:
                msb.showerror("Error", "Ingrese un valor numerico para continuar")
            
            try:
                if float(cajaIteraciones.get()) == 0:
                    msb.showerror("Error", "Ingrese un valor diferente de 0 para continuar")
            except:
                msb.showerror("Error", "Ingrese un valor numerico para continuar")
            
            g = Programa_punto_fijo()
            lista = g.Procedimiento_punto_fijo(cajafuncion.get(), float(cajaX0.get()), float(cajaTolerancia.get()), int(cajaIteraciones.get()))
            
            r =Resultados()
            r.mostrar(lista)


        
        boption = Button(punto_fijo_window, text="Ingresar", bg='#CCD9CE', command=opciones, font="Times",borderwidth=0)
        boption.grid(row=5, column=0, columnspan=2, padx=20, pady=15)
        boption.config(activebackground="#94A9B9", width="16", height="1")

        punto_fijo_window.mainloop()

if __name__ == '__main__':
    ventana = entorno_punto_fijo()
    ventana.principal_punto_fijo()