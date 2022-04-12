#crea una ventana igual a Unidad_3
from tkinter import *
from tkinter import ttk
from unicodedata import name

class unidad_4:
    def Gui_unidad_4(self):
        # Crea una ventana igual a la unidad 2
        self.winu4 = Toplevel()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = self.winu4.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winu4.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winu4.geometry(posicion)
        self.winu4.title('Estructura de datos - Unidad 4')
        self.winu4.config(bg='#7FADA9')
        self.winu4.resizable(0, 0)

        lblTitulo = Label(self.winu4, text="Unidad 4: Derivadas numericas", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options = ["Series de Taylor",
                    "Metodo del trapecio",
                    "Metodo de Simpson 1/3",
                    "Metodo de Simpson 3/8",
                    ]
        
        desplegable_unidad_3 = ttk.Combobox(self.winu4, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_3.place(relx=0.215,rely=0.475)
        desplegable_unidad_3.current(0)

        def funciones():
            pass

        btnAceptar = Button(self.winu4, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.place(relx=0.28, rely=0.8)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        self.winu4.mainloop()

if __name__ == "__main__":
    unidad_4().Gui_unidad_4()