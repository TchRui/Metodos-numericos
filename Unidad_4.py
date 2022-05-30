#crea una ventana igual a Unidad_3
from tkinter import *
from tkinter import ttk
from unicodedata import name

from GUI_Taylor import Gui_Taylor
from GUI_Trapecio import Gui_Trapecio
from GUI_Simpson13 import Gui_Simpson13
from GUI_Simpson38 import Gui_Simpson38
from GUI_Gauss import Gui_Gauss_Seidel
from GUI_3_puntos import Gui_tres_puntos
from GUI_5_puntos import Gui_5_puntos
class unidad_4:
    def Gui_unidad_4(self):
        # Crea una ventana igual a la unidad 2
        self.winu4 = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = self.winu4.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winu4.winfo_screenheight() // 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winu4.geometry(posicion)
        self.winu4.title('Estructura de datos - Unidad 4')
        self.winu4.config(bg='#7FADA9')
        self.winu4.resizable(0, 0)

        lblTitulo = Label(self.winu4, text="Unidad 4: funciones numericas", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        
        options = ["Series de Taylor",
                    "Metodo del trapecio",
                    "Metodo de Simpson 1/3",
                    "Metodo de Simpson 3/8",
                    "Cuadratura de Gauss",
                    "Metodo de 3 puntos",
                    "Metodo de 5 puntos"
                    ]
        
        desplegable_unidad_3 = ttk.Combobox(self.winu4, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_3.place(relx=0.215,rely=0.475)
        desplegable_unidad_3.current(0)

        def funciones():
            if desplegable_unidad_3.get() == "Series de Taylor":
                a = Gui_Taylor()
                a.GUI()
            
            if desplegable_unidad_3.get() == "Metodo del trapecio":
                b = Gui_Trapecio()
                b.GUI()
            
            if desplegable_unidad_3.get() == "Metodo de Simpson 1/3":
                c = Gui_Simpson13()
                c.GUI()
            
            if desplegable_unidad_3.get() == "Metodo de Simpson 3/8":
                d = Gui_Simpson38()
                d.GUI()
            
            if desplegable_unidad_3.get() == "Cuadratura de Gauss":
                e = Gui_Gauss_Seidel()
                e.GUI()
            
            if desplegable_unidad_3.get() == "Metodo de 3 puntos":
                f = Gui_tres_puntos()
                f.procedimiento_tres_puntos()
            
            if desplegable_unidad_3.get() == "Metodo de 5 puntos":
                g = Gui_5_puntos()
                g.procedimiento_cinco_puntos()

        btnAceptar = Button(self.winu4, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.place(relx=0.28, rely=0.8)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        self.winu4.mainloop()

if __name__ == "__main__":
    unidad_4().Gui_unidad_4()