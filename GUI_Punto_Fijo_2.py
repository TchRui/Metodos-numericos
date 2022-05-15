
from tkinter import *
from tkinter import messagebox
import sympy as sp

from ProgramaFijo import Programa_Punto_Fijo
from GUI_Resultados import Resultados

class GUI_Punto_fijo:
    def Interfaz(self):
        #Crea una ventana igual a GUI_Newton
        gui = Toplevel()
        ancho_ventana = 400
        alto_ventana = 550

        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = (gui.winfo_screenheight() // 2 - alto_ventana // 2) - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)

        gui.title('Metodo de Newton-Raphson')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)
        
        lblTitulo = Label(gui, text="Metodo del Punto fijo", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=10, pady=15)

        lblfuncion1 = Label(gui, text="f1(x,y)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion1.grid(row=2, column=0, padx=20, pady=15)

        cajaf1 = Variable()
        cajaf1 = Entry(gui, width=20, textvariable=cajaf1, font="Times",justify="center")
        cajaf1.grid(row=2, column=1, padx=20, pady=15)

        lblfuncion2 = Label(gui, text="f1 despejada", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion2.grid(row=3, column=0, padx=20, pady=15)

        cajaf2 = Variable()
        cajaf2 = Entry(gui, width=20, textvariable=cajaf2, font="Times",justify="center")
        cajaf2.grid(row=3, column=1, padx=20, pady=15)

        lblfuncion3 = Label(gui, text="f2(x,y)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion3.grid(row=4, column=0, padx=20, pady=15)

        cajaf3 = Variable()
        cajaf3 = Entry(gui, width=20, textvariable=cajaf3, font="Times",justify="center")
        cajaf3.grid(row=4, column=1, padx=20, pady=15)

        lblfuncion4 = Label(gui, text="f2 despejada", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion4.grid(row=5, column=0, padx=20, pady=15)

        cajaf4 = Variable()
        cajaf4 = Entry(gui, width=20, textvariable=cajaf4, font="Times",justify="center")
        cajaf4.grid(row=5, column=1, padx=20, pady=15)

        lblx = Label(gui, text="x", bg="#CCD9CE", font="Times", width="10", height="1")
        lblx.grid(row=6, column=0, padx=20, pady=15)

        cajax = Variable()
        cajax = Entry(gui, width=20, textvariable=cajax, font="Times",justify="center")
        cajax.grid(row=6, column=1, padx=20, pady=15)
        
        lbly = Label(gui, text="y", bg="#CCD9CE", font="Times", width="10", height="1")
        lbly.grid(row=7, column=0, padx=20, pady=15)

        cajay = Variable()
        cajay = Entry(gui, width=20, textvariable=cajay, font="Times",justify="center")
        cajay.grid(row=7, column=1, padx=20, pady=15)

        lbliteraciones = Label(gui, text="Iteraciones", bg="#CCD9CE", font="Times", width="10", height="1")
        lbliteraciones.grid(row=8, column=0, padx=20, pady=15)

        cajaiteraciones = Variable()
        cajaiteraciones = Entry(gui, width=20, textvariable=cajaiteraciones, font="Times",justify="center")
        cajaiteraciones.grid(row=8, column=1, padx=20, pady=15)

        def recolector():
            f1 = cajaf1.get()
            f1desp = cajaf2.get()
            f2 = cajaf3.get()
            f2desp = cajaf4.get()

            iteraciones = cajaiteraciones.get()

            if f1 == "":
                messagebox.showerror("Error", "Ingrese la funcion 1")
                
            if f1desp == "":
                messagebox.showerror("Error", "Ingrese la funcion 2 despejada")
            
            if f2 == "":
                messagebox.showerror("Error", "Ingrese la funcion 2")
            
            if f2desp == "":
                messagebox.showerror("Error", "Ingrese la funcion 2 despejada")

            try:
                x = float(cajax.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico en x")
            
            try:
                y = float(cajay.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico en y")

            if iteraciones == "":
                messagebox.showerror("Error", "Ingrese el numero de iteraciones")
            

            N = Programa_Punto_Fijo()
            lista = N.procedimiento_punto_fijo(f1,f2,f1desp,f2desp,x,y,iteraciones)

            for i in range(len(lista)):
                print(lista[i])
            R = Resultados()
            R.mostrar(lista)

        btnCalcular = Button(gui, text="Calcular", bg="#CCD9CE", font="Times", command=recolector)
        btnCalcular.grid(row=9, column=0,columnspan=2, padx=20, pady=15)

        gui.mainloop()

if __name__ == "__main__":
    gui = GUI_Punto_fijo()
    gui.Interfaz()