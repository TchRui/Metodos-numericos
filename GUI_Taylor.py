from tkinter import *
from tkinter import messagebox

from ProgramaTaylor import Programa_Taylor

class Gui_Taylor:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Estructura de datos - Unidad 4')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Series de Taylor", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        lblfuncion2 = Label(gui, text="f(x)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion2.grid(row=1, column=0, padx=20, pady=15)

        cajafuncion = Variable()
        cajafuncion = Entry(gui, width=20, textvariable=cajafuncion, font="Times",justify="center")      
        cajafuncion.grid(row=1, column=1, padx=20, pady=15)

        lblx = Label(gui, text="x", bg="#CCD9CE", font="Times", width="10", height="1")
        lblx.grid(row=2, column=0, padx=20, pady=15)

        cajax = Variable()
        cajax = Entry(gui, width=20, textvariable=cajax, font="Times",justify="center")
        cajax.grid(row=2, column=1, padx=20, pady=15)

        lblh = Label(gui, text="h", bg="#CCD9CE", font="Times", width="10", height="1")
        lblh.grid(row=3, column=0, padx=20, pady=15)

        cajah = Variable()
        cajah = Entry(gui, width=20, textvariable=cajah, font="Times",justify="center")
        cajah.grid(row=3, column=1, padx=20, pady=15)
        
        def funciones():
            funcion = cajafuncion.get()
            x = float(cajax.get())
            h = float(cajah.get())

            if funcion == "":
                messagebox.showerror("Error", "Ingrese la funcion a derivar")

            try:
                if x == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para x")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para x")
                cajax.delete(0, END)

            try:
                if h == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para h")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para h")
                cajah.delete(0, END)

            Programa_Taylor().Procedimiento_Taylor(funcion, x, h)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=4, column=0, columnspan=2, padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    Gui_Taylor().GUI()
        