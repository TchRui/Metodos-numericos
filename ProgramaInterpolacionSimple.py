from tkinter import *
from tkinter import messagebox

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
        gui.title('Estructura de datos - Unidad 4')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Series de Taylor", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=75, pady=15)

        lblfuncion = Label(gui, text="f(x)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion.grid(row=1, column=0, padx=20, pady=15)

        cajafuncion = Variable()
        cajafuncion = Entry(gui, width=15, textvariable=cajafuncion, font="Times",justify="center")
        cajafuncion.grid(row=1, column=1, padx=20, pady=15)

        lblxl = Label(gui, text="xl", bg="#CCD9CE", font="Times", width="10", height="1")
        lblxl.grid(row=2, column=0, padx=20, pady=15)

        cajaxl = Variable()
        cajaxl = Entry(gui, width=15, textvariable=cajaxl, font="Times",justify="center")
        cajaxl.grid(row=2, column=1, padx=20, pady=15)

        lblxu = Label(gui, text="xu", bg="#CCD9CE", font="Times", width="10", height="1")
        lblxu.grid(row=3, column=0, padx=20, pady=15)

        cajaxu = Variable()
        cajaxu = Entry(gui, width=15, textvariable=cajaxu, font="Times",justify="center")
        cajaxu.grid(row=3, column=1, padx=20, pady=15)

        lbltol = Label(gui, text="Tolerancia", bg="#CCD9CE", font="Times", width="10", height="1")
        lbltol.grid(row=4, column=0, padx=20, pady=15)
        
        cajatol = Variable()
        cajatol = Entry(gui, width=15, textvariable=cajatol, font="Times",justify="center")
        cajatol.grid(row=4, column=1, padx=20, pady=15)

        lbliter = Label(gui, text="Iteraciones", bg="#CCD9CE", font="Times", width="10", height="1")
        lbliter.grid(row=5, column=0, padx=20, pady=15)

        cajaiter = Variable()
        cajaiter = Entry(gui, width=15, textvariable=cajaiter, font="Times",justify="center")
        cajaiter.grid(row=5, column=1, padx=20, pady=15)

        def opciones():
            if cajafuncion.get() == "":
                messagebox.showinfo("Error", "Ingrese una función en la caja de texto")
            
            try:
                xl = float(cajaxl.get())
                if xl == 0:
                    messagebox.showinfo("Error", "El valor de xl no puede ser cero")
            except:
                messagebox.showinfo("Error", "El valor de xl no es un número")
                cajaxl.delete(0, END)
        
            try:
                xu = float(cajaxu.get())
                if xu == 0:
                    messagebox.showinfo("Error", "El valor de xu no puede ser cero")
            except:
                messagebox.showinfo("Error", "El valor de xu no es un número")
                cajaxu.delete(0, END)
            
            try:
                tol = float(cajatol.get())
                if tol == 0:
                    messagebox.showinfo("Error", "El valor de la tolerancia no puede ser cero")
            except:
                messagebox.showinfo("Error", "El valor de la tolerancia no es un número")
                cajatol.delete(0, END)
            
            try:
                iteraciones = int(cajaiter.get())
                if iteraciones == 0:
                    messagebox.showinfo("Error", "El valor de las iteraciones no puede ser cero")
            except:
                messagebox.showinfo("Error", "El valor de las iteraciones no es un número")
                cajaiter.delete(0, END)
            
            p = Programa_biseccion()
            lista = p.Procedimiento_biseccion(cajafuncion.get(), float(xl), float(xu), float(tol), int(iteraciones))

            r = Resultados()
            r.mostrar(lista)
            
        btnAceptar = Button(gui, text="Aceptar", command=opciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=2,padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == '__main__':
    gui = Gui_biseccion()
    gui.GUI()
