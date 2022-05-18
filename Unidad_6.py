from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class unidad_6:
    def Gui_unidad_6:
        winU6 = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = winU6.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = winU6.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        winU6.geometry(posicion)
        winU6.title('Estructura de datos - Unidad 5')
        winU6.config(bg='#7FADA9')
        winU6.resizable(0, 0)

        lblTitulo = Label(winU6, text="Unidad 5: interpolacion", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        options = ["Metodo de Euler",
                    ""
                    ]
        
        desplegable_unidad_3 = ttk.Combobox(winU6, width=21, values=options, state="readonly", font="Times", height="1", justify = "center")
        desplegable_unidad_3.place(relx=0.215,rely=0.475)
        desplegable_unidad_3.current(0)

        def funciones():           
            pass

        btnAceptar = Button(winU6, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.place(relx=0.28, rely=0.8)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        winU6.mainloop() 