from tkinter import *
from tkinter import ttk
from Unidad_2 import unidad_2

class EntornoGrafico:
    def menu(self):
        mainwindow = Tk()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = mainwindow.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = mainwindow.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        mainwindow.geometry(posicion)

        mainwindow.title('Metodos numéricos - Programa integrador')
        mainwindow.config(bg = '#7FADA9')
        
        mainwindow.resizable(0,0)

        
        labeltitiulo = Label(mainwindow, text = "METODOS NUMERICOS", bg = "#CCD9CE", font = "Times", width = "25", height= "2")
        labeltitiulo.place(relx=0.175, rely=0.125)

        options = [
            "Unidad 2",
            "Unidad 3",
            "Unidad 4",
            "Unidad 5",
            "Unidad 6"
        ]
        
        cmb = ttk.Combobox(mainwindow, width=21, values=options, state="readonly", font = "Times", height="1", justify = "center")
        cmb.place(relx=0.215,rely=0.475)
        cmb.current(0)

        def acciones():
            if cmb.get() == "Unidad 2":
                mainwindow.withdraw()
                u = unidad_2
                u.principal_unidad_2(self)

        bunidad = Button(mainwindow, text = "Seleccionar unidad", bg = '#CCD9CE', command = acciones, font = "Times")
        bunidad.place(relx=0.28, rely=0.8)
        bunidad.config(activebackground="#94A9B9", width="16", height="1")
        mainwindow.mainloop()


Entorno = EntornoGrafico()
Entorno.menu()