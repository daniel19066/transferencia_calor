
import math
from tkinter import *

raiz= Tk()#creacion interfaz

miFrame=Frame(raiz,width=500,height=400)#tamaño inicial

miFrame.pack()
#Funcion para calcular el diametro interno y externo en Cedula 40
def calcDiametro(diametro):
    if diametro == '1':
        diamint = 0.087
        diamext = 0.110
    elif diametro == '1(1/4)':
        diamint = 0.115
        diamext = 0.138
    elif diametro == '2':
        diamint = 0.172
        diamext = 0.198
    elif diametro == '2(1/2)':
        diamint = 0.206
        diamext = 0.240
    elif diametro == '3':
        diamint = 0.256
        diamext = 0.292
    elif diametro == '4':
        diamint = 0.336
        diamext = 0.375
    return diamint, diamext
#------------------parte de la interfaz grafic-----------------#
variabletexto=StringVar()

cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel1=Label(miFrame, text='Masa Fluido caliente:')
nombreLabel1.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1,column=1,padx=10,pady=10)
nombreLabel2=Label(miFrame, text='cp caliente:')
nombreLabel2.grid(row=1,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=3,column=1,padx=10,pady=10)
nombreLabel3=Label(miFrame, text='temeparatura 1 de fluido caliente:')
nombreLabel3.grid(row=3,column=0,padx=10,pady=10)
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=4,column=1,padx=10,pady=10)
nombreLabel4=Label(miFrame, text='temperatura 2 de fluido caliente:')
nombreLabel4.grid(row=4,column=0,padx=10,pady=10)
cuadroTexto5=Entry(miFrame)
cuadroTexto5.grid(row=5,column=1,padx=10,pady=10)
nombreLabel5=Label(miFrame, text='temperatura 1 fluido frio:')
nombreLabel5.grid(row=5,column=0,padx=10,pady=10)
cuadroTexto6=Entry(miFrame)
cuadroTexto6.grid(row=6,column=1,padx=10,pady=10)
nombreLabel6=Label(miFrame, text='temperatura 2 fluido frio:')
nombreLabel6.grid(row=6,column=0,padx=10,pady=10)
cuadroTexto7=Entry(miFrame)
cuadroTexto7.grid(row=2,column=1,padx=10,pady=10)
nombreLabel7=Label(miFrame, text='cp fluido frio:')
nombreLabel7.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto8=Entry(miFrame)
cuadroTexto8.grid(row=7,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='diametro tubo :')
nombreLabel8.grid(row=7,column=0,padx=10,pady=10)
cuadroTexto9=Entry(miFrame)
cuadroTexto9.grid(row=8,column=1,padx=10,pady=10)
nombreLabel9=Label(miFrame, text='diametro anulo:')
nombreLabel9.grid(row=8,column=0,padx=10,pady=10)

#---------------funcion que llama el boton para calcular todo-----------#
def codigoBoton():
    
    masa1 = float(cuadroTexto1.get())#100000 #float(input("Ingrese masa1: "))
    cp1 = float(cuadroTexto2.get())#0.44 #float(input("Ingrese cp1: "))
    cp2 = float(cuadroTexto7.get()) #0.48 #float(input("Ingrese cp2: "))
    th1 = float(cuadroTexto3.get())#325 #float(input("Ingrese Th1: "))
    th2 =  float(cuadroTexto4.get())#275 #float(input("Ingrese Th2: "))
    tc1 = float(cuadroTexto5.get())#100 #float(input("Ingrese Tc1: "))
    tc2 =  float(cuadroTexto6.get())#300 #float(input("Ingrese Tc2: "))
    calorQ = abs(masa1*cp1*(th2-th1))
    masa2 = abs(calorQ/(cp2*(tc2-tc1)))
    print(masa1)
    print(cp1)
    print(cp2)
    print(th1)
    print(th2)
    print(tc1)
    print(tc2)

    # 1) Calcular la LMTD
    lmtd = ((th2-tc1)-(th1-tc2))/math.log((th2-tc1)/(th1-tc2))

    # 3) Seleccionar el diametro interior y exterior segun el nominal
    diametro1 = cuadroTexto8.get() #input("Ingrese diametro1: ")
    diametro2 = cuadroTexto9.get() #input("Ingrese diametro2: ")
    diamint1, diamext1 = calcDiametro(diametro1)
    diamint2, diamext2 = calcDiametro(diametro2)
    print(diametro1)
    print(diametro2)

    # 4) Calculo de areas
    areaflujo1 = math.pi*((diamint1/2)**2)
    areaflujo2 = math.pi*(((diamint2/2)**2)-((diamext1/2)**2))
    dft = ((diamint2**2)-(diamext1**2))/diamext1
    dcomita = diamint2 - diamext1
    print(areaflujo1)
    print(areaflujo2)
    print(dft)
    print(dcomita)



botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()


raiz.mainloop()

