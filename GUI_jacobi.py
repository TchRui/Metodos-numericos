from tkinter import *
from tkinter import ttk

class Gui_metodo_jacobi:
    def procedimiento_jacobi(self):
        #crea una ventana igual a sustitucion
        self.winJacobi = Tk()
        ancho_ventana = 625
        alto_ventana = 450

        x_ventana = self.winJacobi.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winJacobi.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winJacobi.geometry(posicion)

        self.winJacobi.title('Metodo de Jacobi')
        self.winJacobi.config(bg='#7FADA9')
        self.winJacobi.resizable(0, 0)

        lblTitulo = Label(self.winJacobi, text="Metodo de Jacobi", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=10, padx=10, pady=15)

        lblx1 = Label(self.winJacobi, text="x1", bg="#CCD9CE", font="Times", width="5", height="1")
        lblx1.grid(row=1, column=0, padx=10, pady=15)

        caja_x1 = StringVar()
        caja_x1 = Entry(self.winJacobi, width="5", textvariable=caja_x1,font="Times",justify="center")
        caja_x1.grid(row=1, column=1, padx=10, pady=15)

        lblx2 = Label(self.winJacobi, text="x2", bg="#CCD9CE", font="Times", width="5", height="1")
        lblx2.grid(row=2, column=0, padx=10, pady=15)

        caja_x2 = StringVar()
        caja_x2 = Entry(self.winJacobi, width="5", textvariable=caja_x2,font="Times",justify="center")
        caja_x2.grid(row=2, column=1, padx=10, pady=15)

        lblx3 = Label(self.winJacobi, text="x3", bg="#CCD9CE", font="Times", width="5", height="1")
        lblx3.grid(row=3, column=0, padx=10, pady=15)

        caja_x3 = StringVar()
        caja_x3 = Entry(self.winJacobi, width="5", textvariable=caja_x3,font="Times",justify="center")
        caja_x3.grid(row=3, column=1, padx=10, pady=15)

        lbly1 = Label(self.winJacobi, text="y1", bg="#CCD9CE", font="Times", width="5", height="1")
        lbly1.grid(row=1, column=2, padx=10, pady=15)

        caja_y1 = StringVar()
        caja_y1 = Entry(self.winJacobi, width="5", textvariable=caja_y1,font="Times",justify="center")
        caja_y1.grid(row=1, column=3, padx=10, pady=15)

        lbly2 = Label(self.winJacobi, text="y2", bg="#CCD9CE", font="Times", width="5", height="1")
        lbly2.grid(row=2, column=2, padx=10, pady=15)

        caja_y2 = StringVar()
        caja_y2 = Entry(self.winJacobi, width="5", textvariable=caja_y2,font="Times",justify="center")
        caja_y2.grid(row=2, column=3, padx=10, pady=15)

        lbly3 = Label(self.winJacobi, text="y3", bg="#CCD9CE", font="Times", width="5", height="1")
        lbly3.grid(row=3, column=2, padx=10, pady=15)

        caja_y3 = StringVar()
        caja_y3 = Entry(self.winJacobi, width="5", textvariable=caja_y3,font="Times",justify="center")
        caja_y3.grid(row=3, column=3, padx=10, pady=15)

        lblz1 = Label(self.winJacobi, text="z1", bg="#CCD9CE", font="Times", width="5", height="1")
        lblz1.grid(row=1, column=4, padx=10, pady=15)

        caja_z1 = StringVar()
        caja_z1 = Entry(self.winJacobi, width="5", textvariable=caja_z1,font="Times",justify="center")
        caja_z1.grid(row=1, column=5, padx=10, pady=15)

        lblz2 = Label(self.winJacobi, text="z2", bg="#CCD9CE", font="Times", width="5", height="1")
        lblz2.grid(row=2, column=4, padx=10, pady=15)

        caja_z2 = StringVar()
        caja_z2 = Entry(self.winJacobi, width="5", textvariable=caja_z2,font="Times",justify="center")
        caja_z2.grid(row=2, column=5, padx=10, pady=15)

        lblz3 = Label(self.winJacobi, text="z3", bg="#CCD9CE", font="Times", width="5", height="1")
        lblz3.grid(row=3, column=4, padx=10, pady=15)

        caja_z3 = StringVar()
        caja_z3 = Entry(self.winJacobi, width="5", textvariable=caja_z3,font="Times",justify="center")
        caja_z3.grid(row=3, column=5, padx=10, pady=15)

        lblr1 = Label(self.winJacobi, text="=", bg="#CCD9CE", font="Times", width="5", height="1")
        lblr1.grid(row=1, column=6, padx=10, pady=15)

        caja_r1 = StringVar()
        caja_r1 = Entry(self.winJacobi, width="5", textvariable=caja_r1,font="Times",justify="center")
        caja_r1.grid(row=1, column=7, padx=10, pady=15)

        lblr2 = Label(self.winJacobi, text="=", bg="#CCD9CE", font="Times", width="5", height="1")
        lblr2.grid(row=2, column=6, padx=10, pady=15)

        caja_r2 = StringVar()
        caja_r2 = Entry(self.winJacobi, width="5", textvariable=caja_r2,font="Times",justify="center")
        caja_r2.grid(row=2, column=7, padx=10, pady=15)

        lblr3 = Label(self.winJacobi, text="=", bg="#CCD9CE", font="Times", width="5", height="1")
        lblr3.grid(row=3, column=6, padx=10, pady=15)

        caja_r3 = StringVar()
        caja_r3 = Entry(self.winJacobi, width="5", textvariable=caja_r3,font="Times",justify="center")
        caja_r3.grid(row=3, column=7, padx=10, pady=15)

        self.winJacobi.mainloop()

        
if __name__ == "__main__":
    gui = Gui_metodo_jacobi()
    gui.procedimiento_jacobi()
