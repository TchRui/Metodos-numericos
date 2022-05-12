from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

from ProgramaInterpolacionNewton import Programa_Interpolacion_Newton

class Gui_interpolacionNewton2:
    def GUI(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 325
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Estructura de datos - Unidad 5')
        gui.config(bg='#7FADA9')
        gui.resizable(0, 0)

        lblTitulo = Label(gui, text="Interpolacion de Newton", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=4,padx=20, pady=15)

        lblx1 = Label(gui,text="Primer punto", bg="#CCD9CE", font="Times", width="10", height="1")
        lblx1.grid(row=1,column=0,padx=10,pady=15)

        cajax1 = StringVar()
        cajax1 = Entry(gui, width=10, textvariable=cajax1, font="Times",justify="center")
        cajax1.grid(row=1,column=1,padx=20,pady=15)

        cajax2 = StringVar()
        cajax2 = Entry(gui, width=10, textvariable=cajax2, font="Times",justify="center")
        cajax2.grid(row=1,column=2,padx=20,pady=15)

        lbly1 = Label(gui,text="Segundo punto", bg="#CCD9CE", font="Times", width="10", height="1")
        lbly1.grid(row=2,column=0,padx=10,pady=15)

        cajay1 = StringVar()
        cajay1 = Entry(gui, width=10, textvariable=cajay1, font="Times",justify="center")
        cajay1.grid(row=2,column=1,padx=20,pady=15)

        cajay2 = StringVar()
        cajay2 = Entry(gui, width=10, textvariable=cajay2, font="Times",justify="center")
        cajay2.grid(row=2,column=2,padx=20,pady=15)

        lblz1 = Label(gui,text="Tercer punto", bg="#CCD9CE", font="Times", width="10", height="1")
        lblz1.grid(row=3,column=0,padx=10,pady=15)

        cajaz1 = StringVar()
        cajaz1 = Entry(gui, width=10, textvariable=cajaz1, font="Times",justify="center")
        cajaz1.grid(row=3,column=1,padx=20,pady=15)

        cajaz2 = StringVar()
        cajaz2 = Entry(gui, width=10, textvariable=cajaz2, font="Times",justify="center")
        cajaz2.grid(row=3,column=2,padx=20,pady=15)

        def funciones():
            try:
                x1 = cajax1.get()
                if x1 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El primer punto en su campo x se encuentra vacío")
                else:
                    x1 = int(x1)
                    c1 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")
            
            try:
                x2 = cajax2.get()
                if x2 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El primer punto en su campo f(x) se encuentra vacío")
                else:
                    x2 = int(x2)
                    c2 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")

            try:
                y1 = cajay1.get()
                if y1 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El segundo punto en su campo x se encuentra vacío")
                else:
                    y1 = int(y1)
                    c3 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")
            
            try:
                y2 = cajay2.get()
                if y2 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El segundo punto en su campo f(x) se encuentra vacío")
                else:
                    y2 = int(y2)
                    c4 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")
            
            try:
                z1 = cajaz1.get()
                if z1 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El tercer punto en su campo x se encuentra vacío")
                else:
                    z1 = int(z1)
                    c5 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")
            
            try:
                z2 = cajaz2.get()
                if z2 == "":
                    messagebox.showerror("Interpolacion de Newton","Error: El tercer punto en su campo f(x) se encuentra vacío")
                else:
                    z2 = int(z2)
                    c6 = True
            except ValueError:
                messagebox.showerror("Interpolacion de Newton","Error: Debe ingresar solo valores numéricos.")
            
            if c1 == True and c2 == True and c3 == True and c4 == True and c5 == True and c6 == True:
                lista_valores = [[x1,x2],[y1,y2],[z1,z2]]

                p = Programa_Interpolacion_Newton()
                p.procedimiento_newton(lista_valores)


        btnAceptar = Button(gui, text="Aceptar", command=funciones, width=10, height=1, font="Times", bg = '#CCD9CE')
        btnAceptar.grid(row=6, column=0,columnspan=3,padx=70, pady=15)
        btnAceptar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()

if __name__ == "__main__":
    g = Gui_interpolacionNewton2()
    g.GUI()