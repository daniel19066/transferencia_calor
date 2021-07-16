
import math
from tkinter import *

raiz= Tk()

miFrame=Frame(raiz,width=500,height=400)

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

masa1 = 100000 #float(input("Ingrese masa1: "))
cp1 = 0.44 #float(input("Ingrese cp1: "))
cp2 = 0.48 #float(input("Ingrese cp2: "))
th1 = 325 #float(input("Ingrese Th1: "))
th2 =  275 #float(input("Ingrese Th2: "))
tc1 = 100 #float(input("Ingrese Tc1: "))
tc2 =  300 #float(input("Ingrese Tc2: "))
calorQ = abs(masa1*cp1*(th2-th1))
masa2 = abs(calorQ/(cp2*(tc2-tc1)))

# 1) Calcular la LMTD
lmtd = ((th2-tc1)-(th1-tc2))/math.log((th2-tc1)/(th1-tc2))

# 3) Seleccionar el diametro interior y exterior segun el nominal
diametro1 = '3' #input("Ingrese diametro1: ")
diametro2 = '4' #input("Ingrese diametro2: ")
diamint1, diamext1 = calcDiametro(diametro1)
diamint2, diamext2 = calcDiametro(diametro2)

# 4) Calculo de areas
areaflujo1 = math.pi*((diamint1/2)**2)
areaflujo2 = math.pi*(((diamint2/2)**2)-((diamext1/2)**2))
dft = ((diamint2**2)-(diamext1**2))/diamext1
dcomita = diamint2 - diamext1
print(areaflujo1)
print(areaflujo2)
print(dft)
print(dcomita)



cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='Masa Fluido caliente:')

nombreLabel.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='cp caliente:')
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
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='temperatura 2 fluido frio:')
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='cp fluido frio:')
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='diamtro tubo :')
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
nombreLabel=Label(miFrame, text='diametro anulo:')
masafluidocaliente=0
def codigoBoton():
    masafluidocaliente=cuadroTexto1.get()
    masa1=int(masafluidocaliente)
    print(masafluidocaliente+1)

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()


raiz.mainloop()

