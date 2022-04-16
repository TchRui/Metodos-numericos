from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sympy as sp

from GUI_Resultados import Resultados
from ProgramaSimpson13 import Programa_simpson_1_3

class Gui_Simpson13:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 335
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Estructura de datos - Unidad 4')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Metodo Simpson 1/3", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        lblfuncion2 = Label(gui, text="f'(x)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion2.grid(row=1, column=0, padx=20, pady=15)

        cajafuncion = Variable()
        cajafuncion = Entry(gui, width=20, textvariable=cajafuncion, font="Times",justify="center")      
        cajafuncion.grid(row=1, column=1, padx=20, pady=15)

        lbla = Label(gui, text="a", bg="#CCD9CE", font="Times", width="10", height="1")
        lbla.grid(row=2, column=0, padx=20, pady=15)

        cajaa = StringVar()
        cajaa = Entry(gui, width=20, textvariable=cajaa, font="Times",justify="center")
        cajaa.grid(row=2, column=1, padx=20, pady=15)

        lblb = Label(gui, text="b", bg="#CCD9CE", font="Times", width="10", height="1")
        lblb.grid(row=3, column=0, padx=20, pady=15)

        cajab = StringVar()
        cajab = Entry(gui, width=20, textvariable=cajab, font="Times",justify="center")
        cajab.grid(row=3, column=1, padx=20, pady=15)
        
        
        def funciones():
            funcion = cajafuncion.get()
            a = float(cajaa.get())
            b = float(cajab.get())

            if funcion == "":
                messagebox.showerror("Error", "Ingrese la funcion a derivar")

            try:
                if a == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para x")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para x")
                cajaa.delete(0, END)

            try:
                if b == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para h")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para h")
                cajab.delete(0, END)

            p = Programa_simpson_1_3()
            lista = p.Procedimiento_simpson(funcion, a, b)
        
            for i in lista:
                print(i)
            r = Resultados()
            r.mostrar(lista)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=2,padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    gui = Gui_Simpson13()
    gui.GUI()