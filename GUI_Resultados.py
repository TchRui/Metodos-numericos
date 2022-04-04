from tkinter import *
class Resultados:
    def mostrar(self, lista):
        gui = Tk()
        ancho_ventana = 850
        alto_ventana = 425
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Metodos numericos - ventana de resultados')
        gui.config(bg = '#7FADA9')
        gui.resizable(0,0)

        lbltitulo = Label(gui,text="Resultados de corrida",bg="#c0c1c3",font="Times",width="25",height="2")
        lbltitulo.grid(row=0,column=3,columnspan=4,padx=10,pady=15)

        frameauxiliar = Frame(gui)
        frameauxiliar.grid(row=1,column=0,columnspan=10,padx=30,pady=15)

        scrolly = Scrollbar(frameauxiliar,orient="vertical")
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx = Scrollbar(frameauxiliar,orient="horizontal")
        scrollx.pack(side=BOTTOM,fill=X)

        caja_resultados = Listbox(frameauxiliar,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,font="Times",width="77",height="10")
        caja_resultados.pack(side=LEFT)

        scrolly.config(command=caja_resultados.yview)
        scrollx.config(command=caja_resultados.xview)

        for i in range(len(lista)):
            caja_resultados.insert(END,lista[i])


        btnaceptar = Button(gui,text="Aceptar",bg="#c0c1c3",font="Times",width="10",height="1",command=gui.destroy)
        btnaceptar.grid(row=2,column=3,columnspan=4,padx=10,pady=15)
        gui.mainloop()

if __name__ == "__main__":
    r = Resultados()
    r.mostrar()