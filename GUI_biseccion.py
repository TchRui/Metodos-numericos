from tkinter import *
from tkinter import messagebox
from unicodedata import name

from ProgramaBiseccion import Programa_biseccion
from GUI_Resultados import Resultados

class Gui_biseccion:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 435
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = (gui.winfo_screenheight() // 2 - alto_ventana // 2) - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)

        gui.title('Estructura de datos - Unidad 2')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Metodo de Biseccion", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        lblfuncion2 = Label(gui, text="Función", bg="#CCD9CE", font="Times", width="10", height="1")
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

        lbltol = Label(gui,text="Tolerancia",bg="#CCD9CE", font="Times", width="10", height="1")
        lbltol.grid(row=4,column=0,padx=20,pady=15)

        cajatol = StringVar()
        cajatol = Entry(gui,width=20, textvariable=cajatol, font="Times",justify="center")
        cajatol.grid(row=4,column=1,padx=20,pady=15)

        lbliter = Label(gui,text="Iteraciones",bg="#CCD9CE", font="Times", width="10", height="1")
        lbliter.grid(row=5,column=0,padx=20,pady=15)

        cajaiter = StringVar()
        cajaiter = Entry(gui,width=20, textvariable=cajaiter, font="Times",justify="center")
        cajaiter.grid(row=5,column=1,padx=20,pady=15)
        
        
        def funciones():
            funcion = cajafuncion.get()

            if funcion == "":
                messagebox.showerror("Error", "El campo función se encuentra vacío")

            try:
                a = float(cajaa.get())
                if a == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para a")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para a")
                cajaa.delete(0, END)

            try:
                b = float(cajab.get())
                if b == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para b")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para b")
                cajab.delete(0, END)

            try:
                tolerancia = float(cajatol.get())
                if tolerancia == "":
                    messagebox.showerror("Error","Ingrese un valor válido para la tolerancia")
                
                elif tolerancia <= 0:
                    messagebox.showerror("Error","La tolerancia no puede tener un valor menor a cero")

            except ValueError:
                messagebox.showerror("Error","Solo debe de usar caractéres numéricos válidos")
            
            try:
                iteraciones = int(cajaiter.get())
                if iteraciones == "":
                    messagebox.showerror("Error","Ingrese un valor valido para las iteraciones")
                elif iteraciones <= 0:
                    messagebox.showerror("Error","La cantidad de iteraciones no puede ser menor a cero")
            except ValueError:
                messagebox.showerror("Error","Solo debe usar caractéres numéricos válidos")

            p = Programa_biseccion()
            lista = p.Procedimiento_biseccion(funcion,a,b,tolerancia,iteraciones)
        
            r = Resultados()
            r.mostrar(lista)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=2,padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    g = Gui_biseccion()
    g.GUI()