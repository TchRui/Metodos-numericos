from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

from ProgramaRegresionLineal import Programa_regresion_lineal
class Gui_cuadrados_minimos:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 625
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = (gui.winfo_screenheight() // 2 - alto_ventana // 2) - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Estructura de datos - Unidad 4')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Cuadrados mínimos", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

       
        lblx = Label(gui, text="x", bg="#CCD9CE", font="Times", width="15", height="1")
        lblx.grid(row=1, column=0,padx=20, pady=15)

        lbly = Label(gui, text="y", bg="#CCD9CE", font="Times", width="15", height="1")
        lbly.grid(row=1, column=1,padx=20, pady=15)
        
        #Definiendo las variables para el tamaño de los widgets
        longitud_listbox = 13
        altura_listbox = 8
        longitud_cajas = 10

        #Creamos la lsitbox para contener los valores de x
        frameaxuiliar = Frame(gui)
        frameaxuiliar.grid(row=2, column=0, padx=20, pady=15)

        Scrolly = Scrollbar(frameaxuiliar, orient=VERTICAL)
        Scrolly.pack(side=RIGHT, fill=Y)

        Scrollx = Scrollbar(frameaxuiliar, orient=HORIZONTAL)
        Scrollx.pack(side=BOTTOM, fill=X)

        caja_x = Listbox(frameaxuiliar, width=longitud_listbox, height=altura_listbox,font="Times", justify=CENTER, yscrollcommand=Scrolly.set, xscrollcommand=Scrollx.set,borderwidth=0)
        caja_x.pack(side=LEFT, fill=BOTH)

        Scrolly.config(command=caja_x.yview)
        Scrollx.config(command=caja_x.xview)

        #Creamos la listbox para contener los valores de y
        frameaxuiliar2 = Frame(gui)
        frameaxuiliar2.grid(row=2, column=1, padx=20, pady=15)

        Scrolly2 = Scrollbar(frameaxuiliar2, orient=VERTICAL)
        Scrolly2.pack(side=RIGHT, fill=Y)

        Scrollx2 = Scrollbar(frameaxuiliar2, orient=HORIZONTAL)
        Scrollx2.pack(side=BOTTOM, fill=X)

        caja_y = Listbox(frameaxuiliar2, width=longitud_listbox, height=altura_listbox,font="Times", justify=CENTER,yscrollcommand=Scrolly2.set, xscrollcommand=Scrollx2.set,borderwidth=0)
        caja_y.pack(side=LEFT, fill=BOTH, expand=True)

        Scrolly2.config(command=caja_y.yview)
        Scrollx2.config(command=caja_y.xview)


        #Creamos el boton para agregar los valores de x
        caja_ingreso_x = Variable()
        caja_ingreso_x = Entry(gui, width=longitud_cajas, textvariable=caja_ingreso_x, font="Times", justify=CENTER)
        caja_ingreso_x.grid(row=3, column=0, padx=20, pady=15)

        lista_valores_x = []
        def agregar_x():
            try:
                valor_agregar_x = float(caja_ingreso_x.get())
                if valor_agregar_x == "":
                    messagebox.showinfo("Error", "Debe ingresar un valor")

                else:
                    caja_x.insert(END, valor_agregar_x)
                    caja_ingreso_x.delete(0, END)
                    lista_valores_x.append(valor_agregar_x)

            except ValueError:
                messagebox.showinfo("Error", "Debe ingresar un valor numerico")
                caja_ingreso_x.delete(0, END)

        btnAgregar_x = Button(gui, text="Agregar x", bg="#CCD9CE", font="Times", width="10", height="1", borderwidth=0, command=agregar_x)
        btnAgregar_x.grid(row=4, column=0, padx=20, pady=15)

        #Creamos el boton para eliminar los valores de x

        def eliminar_x():
        
            numero_eliminar_x = simpledialog.askfloat("Eliminar", "Ingrese el numero a eliminar")
            if numero_eliminar_x == "":
                messagebox.showinfo("Error", "Debe ingresar un valor")
            else:
                try:
                    lista_valores_x.remove(numero_eliminar_x)
                    caja_x.delete(0, END)
                    for i in lista_valores_x:
                        caja_x.insert(END, i)
                    messagebox.showinfo("Eliminar", "Valor eliminado correctamente")

                except ValueError:
                   messagebox.showinfo("Error", "El valor no existe dentro de esta lista")
            

        btnElimiar_x = Button(gui, text="Eliminar x", bg="#CCD9CE", font="Times", width="10", height="1", borderwidth=0, command=eliminar_x)
        btnElimiar_x.grid(row=5, column=0, padx=20, pady=15)

        #Creamos el boton para agregar los valores de y
        caja_ingreso_y = Variable()
        caja_ingreso_y = Entry(gui, width=longitud_cajas, textvariable=caja_ingreso_y, font="Times", justify=CENTER)
        caja_ingreso_y.grid(row=3, column=1, padx=20, pady=15)

        lista_valores_y = []
        def agregar_y():
            try:
                valor_agregar_y = float(caja_ingreso_y.get())
                if valor_agregar_y == "":
                    messagebox.showinfo("Error", "Debe ingresar un valor")

                else:
                    caja_y.insert(END, valor_agregar_y)
                    caja_ingreso_y.delete(0, END)
                    lista_valores_y.append(valor_agregar_y)

            except ValueError:
                messagebox.showinfo("Error", "Debe ingresar un valor numerico")
                caja_ingreso_y.delete(0, END)
        
        btnAgregar_y = Button(gui, text="Agregar y", bg="#CCD9CE", font="Times", width="10", height="1", borderwidth=0, command=agregar_y)
        btnAgregar_y.grid(row=4, column=1, padx=20, pady=15)

        #Creamos el boton para eliminar los valores de y
        def eliminar_y():
            numero_eliminar_y = simpledialog.askfloat("Eliminar", "Ingrese el numero a eliminar")
            if numero_eliminar_y == "":
                messagebox.showinfo("Error", "Debe ingresar un valor")
            else:
                try:
                    lista_valores_y.remove(numero_eliminar_y)
                    caja_y.delete(0, END)
                    for i in lista_valores_y:
                        caja_y.insert(END, i)
                    messagebox.showinfo("Eliminar", "Valor eliminado correctamente")

                except ValueError:
                   messagebox.showinfo("Error", "El valor no existe dentro de esta lista")

        btnElimiar_y = Button(gui, text="Eliminar y", bg="#CCD9CE", font="Times", width="10", height="1", borderwidth=0, command=eliminar_y)
        btnElimiar_y.grid(row=5, column=1, padx=20, pady=15)
        
        def funciones():
            if len(lista_valores_x) == 0 or len(lista_valores_y) == 0:
                messagebox.showinfo("Error", "Debe ingresar valores en las listas")
            elif len(lista_valores_x) != len(lista_valores_y):
                messagebox.showinfo("Error", "Las listas no tienen el mismo tamaño")
            else:
                p = Programa_regresion_lineal()
                p.procedimiento_regresion(lista_valores_x, lista_valores_y)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=2,padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1",borderwidth=0)

        gui.mainloop()

if __name__ == "__main__":
    gui = Gui_cuadrados_minimos()
    gui.GUI()