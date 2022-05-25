from tkinter import *
from tkinter import messagebox


from ProgramaEuler import Programa_Euler
from GUI_Resultados import Resultados

class Gui_Euler:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 435
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = (gui.winfo_screenheight() // 2 - alto_ventana // 2) - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)

        gui.title('Estructura de datos - Unidad ')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Metodo de Euler", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        lblfuncion2 = Label(gui, text="Función", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion2.grid(row=1, column=0, padx=20, pady=15)

        cajafuncion = Variable()
        cajafuncion = Entry(gui, width=20, textvariable=cajafuncion, font="Times",justify="center")      
        cajafuncion.grid(row=1, column=1, padx=20, pady=15)

        lblxi = Label(gui, text="x inicial", bg="#CCD9CE", font="Times", width="10", height="1")
        lblxi.grid(row=2, column=0, padx=20, pady=15)

        cajaxi = StringVar()
        cajaxi = Entry(gui, width=20, textvariable=cajaxi, font="Times",justify="center")
        cajaxi.grid(row=2, column=1, padx=20, pady=15)

        lblxe = Label(gui, text="x esperada", bg="#CCD9CE", font="Times", width="10", height="1")
        lblxe.grid(row=3, column=0, padx=20, pady=15)

        cajaxe = StringVar()
        cajaxe = Entry(gui, width=20, textvariable=cajaxe, font="Times",justify="center")
        cajaxe.grid(row=3, column=1, padx=20, pady=15)

        lblyi = Label(gui,text="y inicial",bg="#CCD9CE", font="Times", width="10", height="1")
        lblyi.grid(row=4,column=0,padx=20,pady=15)

        cajayi = StringVar()
        cajayi = Entry(gui,width=20, textvariable=cajayi, font="Times",justify="center")
        cajayi.grid(row=4,column=1,padx=20,pady=15)

        lbliter = Label(gui,text="Iteraciones",bg="#CCD9CE", font="Times", width="10", height="1")
        lbliter.grid(row=5,column=0,padx=20,pady=15)

        cajaiter = StringVar()
        cajaiter = Entry(gui,width=20, textvariable=cajaiter, font="Times",justify="center")
        cajaiter.grid(row=5,column=1,padx=20,pady=15)
        
        
        def funciones():
            f = cajafuncion.get()

            if f == "":
                messagebox.showerror("Error", "El campo función se encuentra vacío")

            try:
                xi = float(cajaxi.get())
                if xi == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para x inicial")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para x inicial")
                cajaxi.delete(0, END)

            try:
                xe = float(cajaxe.get())
                if xe == "":
                    messagebox.showerror("Error", "Ingrese un valor numerico para x esperada")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico para x esperada")
                cajaxe.delete(0, END)

            try:
                yi = float(cajayi.get())
                if yi == "":
                    messagebox.showerror("Error","Ingrese un valor válido para la y inicial")

            except ValueError:
                messagebox.showerror("Error","Solo debe de usar caractéres numéricos válidos")
            
            try:
                n = int(cajaiter.get())
                if n == "":
                    messagebox.showerror("Error","Ingrese un valor valido para las iteraciones")
                elif n <= 0:
                    messagebox.showerror("Error","La cantidad de iteraciones no puede ser menor a cero")
            except ValueError:
                messagebox.showerror("Error","Solo debe usar caractéres numéricos válidos")

            p = Programa_Euler()

            lista = p.Procedimiento_Euler(f,xi,xe,yi,n)

            r = Resultados()
            r.mostrar(lista)

        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=2,padx=20, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    g = Gui_Euler()
    g.GUI()