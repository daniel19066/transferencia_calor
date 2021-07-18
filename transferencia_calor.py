
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
    print(calorQ)

    # 1) Calcular la LMTD
    lmtd = ((th2-tc1)-(th1-tc2))/math.log((th2-tc1)/(th1-tc2))
    print(lmtd)

    # 3) Seleccionar el diametro interior y exterior segun el nominal
    diametro1 = cuadroTexto8.get() #input("Ingrese diametro1: ")
    diametro2 = cuadroTexto9.get() #input("Ingrese diametro2: ")
    diamint1, diamext1 = calcDiametro(diametro1)
    diamint2, diamext2 = calcDiametro(diametro2)

    # 4) Calculo de areas
    areaflujo1 = math.pi*((diamint1/2)**2)
    areaflujo2 = math.pi*(((diamint2/2)**2)-((diamext1/2)**2))
    dft = ((diamint2**2)-(diamext1**2))/diamext1
    dcomita = diamint2 - diamext1

    # 5) Calculo de las propiedades del fluido en tubo
    densidad1 = 74.92
    viscosidadcp1 = 0.23
    viscosidadft1 = viscosidadcp1 * 2.42
    reynolds1 = (masa1*diamint1)/(viscosidadft1*areaflujo1)
    conductividad1 = 0.088
    prandtl1 = (cp1*viscosidadft1)/conductividad1
    nusell1 = ((0.027*(reynolds1**0.8))*(prandtl1**(1/3)))

    hint = (nusell1 * conductividad1)/diamint1
    print(hint)

    # 6) Calculo de las propiedades del fluido en el anulo
    gravespe = 0.88
    densidad2 = gravespe * 62.43
    viscosidadcp2 = 0.18
    viscosidadft2 = viscosidadcp2 * 2.42
    reynolds2 = (masa2*dft)/(viscosidadft2*areaflujo2)
    conductividad2 = 0.087
    prandtl2 = (cp2*viscosidadft2)/conductividad2 
    nusell2 = ((0.027*(reynolds2**0.8))*(prandtl2**(1/3)))

    hext = (nusell2 * conductividad2)/dft
    print(hext)

    # 7) Calculo del area - longitudes, como L es la misma para tubo y anulo
    he = (hext * diamext1) / diamint1
    uclean1 = 1/((1/hint)+(1/he))
    print(uclean1)
    rd1 = 0.004
    diviuclean1 = 0.0027
    udise1 = 1/(rd1 + diviuclean1)
    print(udise1)
    longhor1 = 20 * 2
    areatransferencia1 = calorQ/(lmtd*udise1)
    print(areatransferencia1)
    longcalor1 = (areatransferencia1/(math.pi*diamint1))
    numorquillas1 = math.ceil(areatransferencia1/(math.pi*diamint1*longhor1))
    print(numorquillas1)
    longcorregida1 = numorquillas1*longhor1
    areacorregida1 = numorquillas1*longhor1*math.pi*diamint1
    udisecorregido1 = calorQ/(lmtd*areacorregida1)
    rdfinal1 = (1/udisecorregido1) - (1/uclean1)
    print(rdfinal1)

    hi = (hint*diamint1)/diamext1
    uclean2 = 1/((1/hext)+(1/hi))
    print(uclean2)
    rd2 = 0.004
    diviuclean2 = 1/uclean2
    udise2 = 1/(rd2+diviuclean2)
    print(udise2)
    longhor2 = 20 * 2
    areatransferencia2 = calorQ/(lmtd*udise2)
    print(areatransferencia2)
    longcalor2 = areatransferencia2/(math.pi*diamext1)
    numorquillas2 = math.ceil(areatransferencia2/(math.pi*diamext1*longhor2))
    print(numorquillas2)
    longcorregida2 = numorquillas2*longhor2
    areacorregida2 = numorquillas2*longhor2*math.pi*diamext1
    udisecorregido2 = calorQ/(lmtd*areacorregida2)
    rdfinal2 = (1/udisecorregido2)-(1/uclean2)
    print(rdfinal2)

    # 8) Usando la caida de presion
    f = 0.0035+(0.264/(reynolds1**0.42))
    print(f)
    g = 32.17*(3600**2)
    velmasica = masa1/areaflujo1
    deltaf = (4*f*(velmasica**2)*longcorregida1)/(2*g*(densidad1**2)*diamint1)
    deltap = deltaf*densidad1
    print(deltap)

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()