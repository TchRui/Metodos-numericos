from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sympy as sp

from ProgramaEcuacionesTaylor import Programa_Ecuaciones_Taylor

class Gui_ecuaciones_taylor:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 285
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = (gui.winfo_screenheight() // 2 - alto_ventana // 2) - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Estructura de datos - Ecuaciones de Taylor')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Ecuaciones de Taylor", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=4,padx=20, pady=15)


        lblFuncion = Label(gui, text="Función:", bg="#CCD9CE", font="Times", width="10", height="1")
        lblFuncion.grid(row=1, column=0, padx=20, pady=10)
        
        txtfuncion = Variable()
        txtfuncion = Entry(gui, width=20, textvariable=txtfuncion, font="Times",justify="center")
        txtfuncion.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

        lblN = Label(gui, text="Grado:", bg="#CCD9CE", font="Times", width="10", height="1")
        lblN.grid(row=2, column=0, padx=20, pady=10)

        txtn = Variable()
        txtn = Entry(gui, width=20, textvariable=txtn, font="Times",justify="center")
        txtn.grid(row=2, column=1, columnspan=2, padx=20, pady=10)

        lblH = Label(gui, text="T. de paso:", bg="#CCD9CE", font="Times", width="10", height="1")
        lblH.grid(row=3, column=0, padx=20, pady=10)

        txth = Variable()
        txth = Entry(gui, width=20, textvariable=txth, font="Times",justify="center")
        txth.grid(row=3, column=1, columnspan=2, padx=20, pady=10)
                
        def funciones():
            funcion = txtfuncion.get()
            
            if funcion == "":
                messagebox.showinfo("Error", "Ingrese una función")
            
            try:
                n = float(txtn.get())
                if n <= 0:
                    messagebox.showinfo("Error", "Ingrese un número mayor a 0")
                if n > 3:
                    messagebox.showinfo("Error", "Ingrese un número menor a 3")
            except:
                messagebox.showinfo("Error", "Ingrese un valor numérico")

            try:
                h = float(txth.get())
            except:
                messagebox.showinfo("Error", "Ingrese un valor numérico")

            p = Programa_Ecuaciones_Taylor()
            p.Procedimiento_Ecuaciones_Taylor(funcion, n, h)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=3,padx=70, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    g = Gui_Ecuaciones_Taylor()
    g.GUI()