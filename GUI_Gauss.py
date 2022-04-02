from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np

from ProgramaGauss import Programa_Gauss_Seiel
class GUI_Gauss_Seidel:

    def procedimiento_gauss(self):
        self.winJacobi = Toplevel()
        ancho_ventana = 820
        alto_ventana = 380

        x_ventana = self.winJacobi.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winJacobi.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winJacobi.geometry(posicion)

        self.winJacobi.title('Metodo de Gauss Seidel')
        self.winJacobi.config(bg='#7FADA9')
        self.winJacobi.resizable(0, 0)

        lblTitulo = Label(self.winJacobi, text="Metodo de Gauss seidel", bg="#CCD9CE", font="Times", width="25", height="2")
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

        lbltole = Label(self.winJacobi, text="Tolerancia", bg="#CCD9CE", font="Times", height="1", width="8")
        lbltole.grid(row=4, column=1, padx=10, pady=15,columnspan=1)

        caja_tole = StringVar()
        caja_tole = Entry(self.winJacobi, textvariable=caja_tole,font="Times",justify="center", width="8")
        caja_tole.grid(row=4, column=2, padx=10, pady=15,columnspan=1)

        lblimax = Label(self.winJacobi, text="Iteraciones", bg="#CCD9CE", font="Times", height="1", width="8")
        lblimax.grid(row=4, column=3, padx=10, pady=15,columnspan=1)

        caja_imax = StringVar()
        caja_imax = Entry(self.winJacobi, textvariable=caja_imax,font="Times",justify="center", width="8")
        caja_imax.grid(row=4, column=4, padx=10, pady=15,columnspan=1)

        lbiomega = Label(self.winJacobi, text="Omega", bg="#CCD9CE", font="Times", height="1", width="8")
        lbiomega.grid(row=4, column=5, padx=10, pady=15,columnspan=1)

        caja_omega = StringVar()
        caja_omega = Entry(self.winJacobi, textvariable=caja_omega,font="Times",justify="center", width="8")
        caja_omega.grid(row=4, column=6, padx=10, pady=15,columnspan=1)

        def funcion():
            x1 = caja_x1.get()
            x2 = caja_x2.get()
            x3 = caja_x3.get()
            y1 = caja_y1.get()
            y2 = caja_y2.get()
            y3 = caja_y3.get()
            z1 = caja_z1.get()
            z2 = caja_z2.get()
            z3 = caja_z3.get()
            r1 = caja_r1.get()
            r2 = caja_r2.get()
            r3 = caja_r3.get()
            tole = caja_tole.get()
            imax = caja_imax.get()
            omega = caja_omega.get()
        
            if x1 == "" or x2 == "" or x3 == "" or y1 == "" or y2 == "" or y3 == "" or z1 == "" or z2 == "" or z3 == "" or r1 == "" or r2 == "" or r3 == "" or tole == "" or imax == "" or omega == "":
                messagebox.showerror("Error", "Uno o mas campos estan vacios")
            else:
                try:
                    x1 = float(x1)
                except ValueError:
                    messagebox.showerror("Error", "El valor de x1 no es valido")
                    caja_x1.delete(0, END)
                try:
                    x2 = float(x2)
                except ValueError:
                    messagebox.showerror("Error", "El valor de x2 no es valido")
                    caja_x2.delete(0, END)

                try:
                    x3 = float(x3)
                except ValueError:
                    messagebox.showerror("Error", "El valor de x3 no es valido")
                    caja_x3.delete(0, END)    

                try:
                    y1 = float(y1)
                except ValueError:
                    messagebox.showerror("Error", "El valor de y1 no es valido")
                    caja_y1.delete(0, END)
                
                try:
                    y2 = float(y2)
                except ValueError:
                    messagebox.showerror("Error", "El valor de y2 no es valido")
                    caja_y2.delete(0, END)

                try:
                    y3 = float(y3)
                except ValueError:
                    messagebox.showerror("Error", "El valor de y3 no es valido")
                    caja_y3.delete(0, END)

                try:
                    z1 = float(z1)
                except ValueError:
                    messagebox.showerror("Error", "El valor de z1 no es valido")
                    caja_z1.delete(0, END)

                try:
                    z2 = float(z2)
                except ValueError:
                    messagebox.showerror("Error", "El valor de z2 no es valido")
                    caja_z2.delete(0, END)

                try:
                    z3 = float(z3)
                except ValueError:
                    messagebox.showerror("Error", "El valor de z3 no es valido")
                    caja_z3.delete(0, END)

                try:
                    r1 = float(r1)
                except ValueError:
                    messagebox.showerror("Error", "El valor de r1 no es valido")
                    caja_r1.delete(0, END)

                try:
                    r2 = float(r2)
                except ValueError:
                    messagebox.showerror("Error", "El valor de r2 no es valido")
                    caja_r2.delete(0, END)

                try:
                    r3 = float(r3)
                except ValueError:
                    messagebox.showerror("Error", "El valor de r3 no es valido")
                    caja_r3.delete(0, END)
                
                try:
                    tole = float(tole)
                except ValueError:
                    messagebox.showerror("Error", "El valor de tole no es valido")
                    caja_tole.delete(0, END)
                
                try:
                    imax = float(imax)
                except ValueError:
                    messagebox.showerror("Error", "El valor de imax no es valido")
                    caja_imax.delete(0, END)
                
                try:
                    omega = int(omega)
                except ValueError:
                    messagebox.showerror("Error", "El valor de omega no es valido")
                    caja_omega.delete(0, END)

                '''A = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
                B = [r1,r2,r3]
                n = 3
                print(A)
                print("")
                print(B)
                print("")
                alpha = 3 * n
                ADD = np.dot(A,A.T) + alpha*np.identity(n)
                A = ADD
                x = np.zeros(len(A))
                ea = 10**10000
                tool = tole'''

                n = 3
                A = np.random.rand(n, n)
                B = np.random.rand(n,)    
                x = np.zeros(len(A))
                imax = 200
                tool = 0.0001
                omega = 1

                p = Programa_Gauss_Seiel()
                p.SOR(A,B,x,tole,imax,omega,tool)


        #Boton de calcular
        boton_calcular = Button(self.winJacobi, text="Calcular", bg="#CCD9CE", font="Times", command=funcion, width="10", height="1")
        boton_calcular.grid(row=5, column=0, padx=10, pady=15, columnspan=10)

        self.winJacobi.mainloop()
if __name__ == "__main__":
    g = GUI_Gauss_Seidel()
    g.procedimiento_gauss()
