from tkinter import *

raiz= Tk()

miFrame=Frame(raiz,width=500,height=400)

miFrame.pack()

cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='Masa Fluido caliente:')

nombreLabel.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='Masa Fluido frio:')
nombreLabel.grid(row=1,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=2,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='temeparatura 1 de fluido caliente:')
nombreLabel.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=3,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='temperatura 2 de fluido caliente:')
nombreLabel.grid(row=3,column=0,padx=10,pady=10)
cuadroTexto5=Entry(miFrame)
cuadroTexto5.grid(row=4,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='temperatura 1 fluido frio:')
nombreLabel.grid(row=4,column=0,padx=10,pady=10)
masafluidocaliente=0
def codigoBoton():
    masafluidocaliente=cuadroTexto1.get()
    masafluidocaliente=int(masafluidocaliente)
    print(masafluidocaliente+1)

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()


raiz.mainloop()