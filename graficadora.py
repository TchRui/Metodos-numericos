import tkinter as t
from tkinter import Label, messagebox
from matplotlib.figure import Figure
from matplotlib.pyplot import *
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from math import *
win = t.Tk()
win.title("Metodo gráfico")
win.geometry("800x700")
win.config(bg='#7FADA9')
style.use('fivethirtyeight')
fig = Figure()
ax = fig.add_subplot(111)
cvs = FigureCanvasTkAgg(fig,win)
cvs.draw()
cvs.get_tk_widget().pack(side=t.TOP, fill=t.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(cvs, win)
toolbar.update()
cvs.get_tk_widget().pack(side=t.TOP, fill=t.BOTH, expand=1)
rang1 = False
rang2 = ""
rang3 = ""

fun = {"sin": "np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","log":"np.log","pi":"np.pi"}

def reemplaza(p):
    for i in fun:
        if i in p:
            p = p.replace(i,fun[i])
        return p

def animate(i):
    global rang1
    global rang2

    if rang1 == True:
        try:
            min=float(rang3[0]); max = float(rang3[1])
            if min < max:
                x = np.arange(min,max,0.01)
                rang2 = [min,max]
            else:
                rang1 = False
        except:
            messagebox.showerror("Error","El rango dado de entrada es inválido")
            rang1 = False
            entr_var.delete(0,len(entr_var.get()))
    else:
        if rang2 != "":
            x = np.arange(rang2[0],rang2[1],0.01)
        else:
            x = np.arange(0,10,0.01)
    try:
        sl = eval(graf_dt)
        ax.clear()
        ax.plot(x,sl)
    except:
        ax.plot()
    ax.axhline(0,color="gray")
    ax.axvline(0,color="gray")
    ani.event_source.stop()

def represent():
    global graf_dt
    global rang3
    global rang1

    tx_origl = entra_funcion.get()

    if entr_var.get() != "":
        rann = entr_var.get()
        rang3 = rann.split(",")
        rang1 = True
    graf_dt = reemplaza(tx_origl)
    ani.event_source.start()
ani = anim.FuncAnimation(fig, animate,interval=1000)
show()


boton1 = t.Button(win,text="Graficar", command=represent)

labelfuncion = Label(win,text="Ingrese la funcion:", bg='#7FADA9',font="Times",height="1")
entra_funcion = t.Entry(win, width=40)

labelvariable = Label(win,text="Ingrese el intervalo", bg='#7FADA9',font="Times",height="1")
entr_var = t.Entry(win, width=20)

boton1.pack(side=t.BOTTOM,pady=5)

entr_var.pack(side=t.BOTTOM)
labelvariable.pack(side=t.BOTTOM)

entra_funcion.pack(side=t.BOTTOM)
labelfuncion.pack(side=t.BOTTOM)

win.mainloop()