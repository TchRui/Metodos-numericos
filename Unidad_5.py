from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

from GUI_interpilacion_newton_1 import Gui_interpolacionNewton1
from GUI_interpilacion_newton_2 import Gui_interpolacionNewton2
from GUI_interpilacion_newton_3 import Gui_interpolacionNewton3
from GUI_interpilacion_Lagrange_2 import Gui_interpolacionLagrage2
from GUI_Regresion_lineal import Gui_regresion_lineal
from GUI_Cuadrados_minimos import Gui_cuadrados_minimos

class unidad_5:
    def Gui_unidad_5(self):
        # Crea una ventana igual a la unidad 2
        winu5 = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = winu5.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = winu5.winfo_screenheight() // 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        winu5.geometry(posicion)
        winu5.title('Estructura de datos - Unidad 5')
        winu5.config(bg='#7FADA9')
        winu5.resizable(0, 0)

        lblTitulo = Label(winu5, text="Unidad 5: interpolacion", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options = ["Interpolacion de Lagrange",
                    "Interpolacion de Newton",
                    "Regresion y correlacion",
                    "Minimos cuadrados",
                    ]
        
        desplegable_unidad_3 = ttk.Combobox(winu5, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_3.place(relx=0.215,rely=0.475)
        desplegable_unidad_3.current(0)

        def funciones():           
            if desplegable_unidad_3.get() == "Interpolacion de Lagrange":
                g = Gui_interpolacionLagrage2()
                g.GUI()

            if desplegable_unidad_3.get() == "Interpolacion de Newton":
                n = simpledialog.askinteger("Interpolación de Newton","De que longitud será la interpolación de Newton:")

                if n == 1:
                    g = Gui_interpolacionNewton1()
                    g.GUI()

                elif n == 2:
                    g = Gui_interpolacionNewton2()
                    g.GUI()

                elif n == 3:
                    g = Gui_interpolacionNewton3()
                    g.GUI()
                elif n < 1 or n > 3:
                    messagebox.showinfo("Error", "Elija una opción entre 1 y 3")

            if desplegable_unidad_3.get() == "Regresion y correlacion":
                g = Gui_regresion_lineal()
                g.GUI()

            if desplegable_unidad_3.get() == "Minimos cuadrados":
                g = Gui_cuadrados_minimos()
                g.GUI()

        btnAceptar = Button(winu5, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.place(relx=0.28, rely=0.8)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        winu5.mainloop()

if __name__ == "__main__":
    unidad_5().Gui_unidad_5()