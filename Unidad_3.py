from tkinter import *
from tkinter import ttk

from GUI_jacobi import Gui_metodo_jacobi
from GUI_Gauss import GUI_Gauss_Seidel
from GUI_Newton import GUI_Newton_Raphson
class unidad_3:
    def Gui_unidad_3(self):
        # Crea una ventana igual a la unidad 2
        self.winU3 = Toplevel()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = self.winU3.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winU3.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winU3.geometry(posicion)
        self.winU3.title('Estructura de datos - Unidad 3')
        self.winU3.config(bg='#7FADA9')
        self.winU3.resizable(0, 0)

        lblTitulo = Label(self.winU3, text="Unidad 3:", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options = ["Metodo de jacobi", 
                   "Metodo de Gauss-Seidel", 
                   "Metodo de Newton-Raphson"]
        
        desplegable_unidad_3 = ttk.Combobox(self.winU3, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_3.place(relx=0.215,rely=0.475)
        desplegable_unidad_3.current(0)

        def funciones():
            if desplegable_unidad_3.get() == "Metodo de jacobi":
                j = Gui_metodo_jacobi()
                j.procedimiento_jacobi()

            elif desplegable_unidad_3.get() == "Metodo de Gauss-Seidel":
                g = GUI_Gauss_Seidel()
                g.procedimiento_gauss()

            elif desplegable_unidad_3.get() == "Metodo de Newton-Raphson":
                r = GUI_Newton_Raphson()
                r.interfaz_newton()

        btnAceptar = Button(self.winU3, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.place(relx=0.28, rely=0.8)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        self.winU3.mainloop()