from tkinter import *
from tkinter import messagebox
import sympy as sp

from ProgramaNewton import Programa_Newton
class GUI_Newton_Raphson:
    def interfaz_newton(self):
        x,y,z,w,sin,cos,tan,cot,sec,csc,asin,acos,atan,acot,asec,acsc = sp.symbols('x y z w sin cos tan cot sec csc asin acos atan acot asec acsc')
        self.winNewton = Tk()
        ancho_ventana = 400
        alto_ventana = 425

        x_ventana = self.winNewton.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winNewton.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.winNewton.geometry(posicion)

        self.winNewton.title('Metodo de Newton-Raphson')
        self.winNewton.config(bg='#7FADA9')
        self.winNewton.resizable(0, 0)
        
        lblTitulo = Label(self.winNewton, text="Metodo de Newton", bg="#CCD9CE", font="Times", width="25", height="2")
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=10, pady=15)

        lblfuncion1 = Label(self.winNewton, text="f1(x,y)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion1.grid(row=2, column=0, padx=20, pady=15)

        cajaf1 = Variable()
        cajaf1 = Entry(self.winNewton, width=20, textvariable=cajaf1, font="Times",justify="center")
        cajaf1.grid(row=2, column=1, padx=20, pady=15)

        lblfuncion2 = Label(self.winNewton, text="f2(x,y)", bg="#CCD9CE", font="Times", width="10", height="1")
        lblfuncion2.grid(row=3, column=0, padx=20, pady=15)

        cajaf2 = Variable()
        cajaf2 = Entry(self.winNewton, width=20, textvariable=cajaf2, font="Times",justify="center")
        cajaf2.grid(row=3, column=1, padx=20, pady=15)

        lblx = Label(self.winNewton, text="x", bg="#CCD9CE", font="Times", width="10", height="1")
        lblx.grid(row=4, column=0, padx=20, pady=15)

        cajax = Variable()
        cajax = Entry(self.winNewton, width=20, textvariable=cajax, font="Times",justify="center")
        cajax.grid(row=4, column=1, padx=20, pady=15)
        
        lbly = Label(self.winNewton, text="y", bg="#CCD9CE", font="Times", width="10", height="1")
        lbly.grid(row=5, column=0, padx=20, pady=15)

        cajay = Variable()
        cajay = Entry(self.winNewton, width=20, textvariable=cajay, font="Times",justify="center")
        cajay.grid(row=5, column=1, padx=20, pady=15)

        lbliteraciones = Label(self.winNewton, text="Iteraciones", bg="#CCD9CE", font="Times", width="10", height="1")
        lbliteraciones.grid(row=6, column=0, padx=20, pady=15)

        cajaiteraciones = Variable()
        cajaiteraciones = Entry(self.winNewton, width=20, textvariable=cajaiteraciones, font="Times",justify="center")
        cajaiteraciones.grid(row=6, column=1, padx=20, pady=15)


        def recolector():
            f1 = cajaf1.get()
            f2 = cajaf2.get()
            iteraciones = cajaiteraciones.get()

            if f1 == "":
                messagebox.showerror("Error", "Ingrese la funcion 1")
                
            if f2 == "":
                messagebox.showerror("Error", "Ingrese la funcion 2")

            try:
                x = int(cajax.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico en x")
            
            try:
                y = int(cajay.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numerico en y")

            if iteraciones == "":
                messagebox.showerror("Error", "Ingrese el numero de iteraciones")
            

            N = Programa_Newton()
            N.procedimiento_newton(f1,f2,x,y,iteraciones)

        btnCalcular = Button(self.winNewton, text="Calcular", bg="#CCD9CE", font="Times", command=recolector)
        btnCalcular.grid(row=7, column=0,columnspan=2, padx=10, pady=5)

        self.winNewton.mainloop()

if __name__ == "__main__":
    aplicacion = GUI_Newton_Raphson()
    aplicacion.interfaz_newton()