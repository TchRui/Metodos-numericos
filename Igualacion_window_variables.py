from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb

from Igualacion import igualacion

class entorno_igualacion:
    
    def principal_igualacion(self):
        igualacion_window = Toplevel()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = igualacion_window.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = igualacion_window.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        igualacion_window.geometry(posicion)

        igualacion_window.title('Estructura de datos - Unidad 2')
        igualacion_window.config(bg='#7FADA9')
        igualacion_window.resizable(0, 0)

        lblTitulo = Label(igualacion_window, text="Unidad 2: Método de igualacion", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.place(relx=0.175, rely=0.125)

        lbla = Label(igualacion_window, text = "Ingrese x1:", bg="#CCD9CE", font="Times", width="8", height="1")
        lbla.place(relx=0.115, rely= 0.35)

        caja_1 = IntVar()
        caja_1 = ttk.Entry(igualacion_window, textvariable=caja_1, font="Times", width="5", justify=CENTER)
        caja_1.place(relx=0.35, rely=0.35)

        lblb = Label(igualacion_window, text = "Ingrese y1", bg="#CCD9CE", font="Times", width="8", height="1")
        lblb.place(relx=0.115, rely= 0.5)

        caja_2 = IntVar()
        caja_2 = ttk.Entry(igualacion_window, textvariable=caja_2, font="Times", width="5", justify=CENTER)
        caja_2.place(relx=0.35, rely=0.5)

        lbligl = Label(igualacion_window, text = "Igual a:", bg="#CCD9CE", font="Times", width="8", height="1")
        lbligl.place(relx=0.115, rely= 0.65)

        caja_3 = IntVar()
        caja_3 = ttk.Entry(igualacion_window, textvariable=caja_3, font="Times", width="5", justify=CENTER)
        caja_3.place(relx=0.35, rely=0.65)

        lbld = Label(igualacion_window, text = "Ingrese x2:", bg="#CCD9CE", font="Times", width="8", height="1")
        lbld.place(relx=0.5, rely= 0.35)

        caja_4 = IntVar()
        caja_4 = ttk.Entry(igualacion_window, textvariable=caja_4, font="Times", width="5", justify=CENTER)
        caja_4.place(relx=0.74, rely=0.35)

        lble = Label(igualacion_window, text = "Ingrese y2", bg="#CCD9CE", font="Times", width="8", height="1")
        lble.place(relx=0.5, rely= 0.5)

        caja_5 = IntVar()
        caja_5 = ttk.Entry(igualacion_window, textvariable=caja_5, font="Times", width="5", justify=CENTER)
        caja_5.place(relx=0.74, rely=0.5)

        lbligl_2 = Label(igualacion_window, text = "Igual a:", bg="#CCD9CE", font="Times", width="8", height="1")
        lbligl_2.place(relx=0.5, rely= 0.65)

        caja_6 = IntVar()
        caja_6 = ttk.Entry(igualacion_window, textvariable=caja_6, font="Times", width="5", justify=CENTER)
        caja_6.place(relx=0.74, rely=0.65)

        def opciones():
            try:

                if int(caja_1.get()) != "" and int(caja_2.get()) != "" and int(caja_3.get()) != "" and int(caja_4.get()) != "" and int(caja_5.get()) != "" and int(caja_6.get()) != "":
                    a = float(caja_1.get())
                    b = float(caja_2.get())
                    c = float(caja_3.get())

                    d = float(caja_4.get())
                    e = float(caja_5.get())
                    f = float(caja_6.get())

                    i = igualacion()
                    flag = i.procedimiento_igualacion(a, b, c, d, e, f)

                    if flag == True:
                        pass

                else:
                    msb.showwarning("Aviso","No pueden quedar casillas vacías")

            except ValueError:
                msb.showerror("Error","No se pueden introducir caracteres no numéricos")

        boption = Button(igualacion_window, text="Ingresar", bg='#CCD9CE', command=opciones, font="Times", )
        boption.place(relx=0.28, rely=0.8)
        boption.config(activebackground="#94A9B9", width="16", height="1")

        igualacion_window.mainloop()