# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from tkinter import *
from tkinter import ttk

from Reduccion_window_variables import entorno_reduccion
from Igualacion_window_variables import  entorno_igualacion
from sustitucion_window_variables import entorno_sustitucion
from punto_fijo_ventana import entorno_punto_fijo
import graficadora
class unidad_2:
    def principal_unidad_2(self):
        self.winU2 = Toplevel()
        
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = self.winU2.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winU2.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winU2.geometry(posicion)

        self.winU2.title('Estructura de datos - Unidad 2')
        self.winU2.config(bg='#7FADA9')
        self.winU2.resizable(0, 0)

        lblTitulo = Label(self.winU2, text="Unidad 2:", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options = [
            "Reduccion",
            "Igualacion",
            "Sustitucion",
            "Metodo grafico",
            "Punto fijo",
            "Interpolacion",
            "Biseccion", 
        ]

        desplegable_unidad_2 = ttk.Combobox(self.winU2, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_2.place(relx=0.215,rely=0.475)
        desplegable_unidad_2.current(0)

        def funciones():
            if desplegable_unidad_2.get() == "Reduccion":
                r = entorno_reduccion()
                r.principal_reduccion()
            
            if desplegable_unidad_2.get() == "Igualacion":
                i = entorno_igualacion()
                i.principal_igualacion()

            if desplegable_unidad_2.get() == "Sustitucion":
                s = entorno_sustitucion()
                s.principal_sustitucion()

            if desplegable_unidad_2.get() == "Punto fijo":
                p = entorno_punto_fijo()
                p.principal_punto_fijo()

            if desplegable_unidad_2.get() == "Metodo grafico":
                i = graficadora

            if desplegable_unidad_2.get() == "Interpolacion":
                pass

            if desplegable_unidad_2.get() == "Biseccion":
                pass

        boption = Button(self.winU2, text="Seleccionar Programa", bg='#CCD9CE', command=funciones, font="Times", )
        boption.place(relx=0.28, rely=0.8)
        boption.config(activebackground="#94A9B9", width="16", height="1")

u2 = unidad_2()

