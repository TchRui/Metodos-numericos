from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb

from punto_fijo_exp import procedimiento_exp

class entorno_punto_fijo:
    def principal_punto_fijo(self):
        punto_fijo_window = Toplevel()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = punto_fijo_window.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = punto_fijo_window.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        punto_fijo_window.geometry(posicion)

        punto_fijo_window.title('Estructura de datos - Unidad 2')
        punto_fijo_window.config(bg='#7FADA9')
        punto_fijo_window.resizable(0, 0)

        lblTitulo = Label(punto_fijo_window, text="Unidad 2: Método del punto fijo", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options =["Ecuación exp(-x)-x"]

        cmb = ttk.Combobox(punto_fijo_window, width=21, values=options, state="readonly", font = "Times", height="1", justify = "center")
        cmb.place(relx=0.215,rely=0.475)
        cmb.current(0)

        def opciones():
            if cmb.get() == "Ecuación exp(-x)-x":
                p1 = procedimiento_exp()
                p1.procedimiento()

        boption = Button(punto_fijo_window, text="Ingresar", bg='#CCD9CE', command=opciones, font="Times", )
        boption.place(relx=0.28, rely=0.8)
        boption.config(activebackground="#94A9B9", width="16", height="1")

        punto_fijo_window.mainloop()