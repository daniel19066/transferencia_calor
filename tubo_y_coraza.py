import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
raiz = Tk()#creacion interfaz

miFrame=Frame(raiz,width=500,height=400)#tamaño inicial

miFrame.pack()
#Funcion para calcular el diametro interno y externo en Cedula 40
def calcDiametro(diametro, bwg):
    diamint = 0.0
    if diametro == '3/4':
        if bwg == "10":
            diamint = 0.482
        if bwg == "12":
            diamint = 0.532
        if bwg == "14":
            diamint = 0.584
        if bwg == "16":
            diamint = 0.620
    elif diametro == '1':
        if bwg == "10":
            diamint = 0.732
        if bwg == "12":
            diamint = 0.782
        if bwg == "14":
            diamint = 0.834
        if bwg == "16":
            diamint = 0.870
    elif diametro == '1(1/4)':
        if bwg == "10":
            diamint = 0.982
        if bwg == "12":
            diamint = 1.03
        if bwg == "14":
            diamint = 1.08
        if bwg == "16":
            diamint = 1.12
    return diamint

#-------------------------------------------parte de la interfaz grafica-----------------------------------#

#--------------------------------------input-----------------------------------------------------#
variabletexto=StringVar()
lmtdtexto=StringVar()
hinttexto=StringVar()
hexttexto=StringVar()
uclean1texto=StringVar()
udiseno1texto=StringVar()
areatrans1texto=StringVar()
numerorq1texto=StringVar()
rdfinal1texto=StringVar()
uclean2texto=StringVar()
udiseno2texto=StringVar()
areatrans2texto=StringVar()
numerorq2texto=StringVar()
rdfinal2texto=StringVar()
deltaptexto=StringVar()
cuadroTexto0=Entry(miFrame)
cuadroTexto0.grid(row=0,column=1,padx=10,pady=10)
nombreLabel0=Label(miFrame, text='densidad fluido del tubo(lb/ft^3):')
nombreLabel0.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=1,column=1,padx=10,pady=10)
nombreLabel1=Label(miFrame, text='densidad fluido coraza(lb/ft^3):')
nombreLabel1.grid(row=1,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=2,column=1,padx=10,pady=10)
nombreLabel2=Label(miFrame, text='cp del fluido del tubo(btu/lb°F):')
nombreLabel2.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=4,column=1,padx=10,pady=10)
nombreLabel3=Label(miFrame, text='cp del fluido coraza(btu/lb°F):')
nombreLabel3.grid(row=4,column=0,padx=10,pady=10)
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=5,column=1,padx=10,pady=10)
nombreLabel4=Label(miFrame, text='viscosidad fluido tubo(cp):')
nombreLabel4.grid(row=5,column=0,padx=10,pady=10)
cuadroTexto5=Entry(miFrame)
cuadroTexto5.grid(row=6,column=1,padx=10,pady=10)
nombreLabel5=Label(miFrame, text='viscosidad fluido coraza(cp):')
nombreLabel5.grid(row=6,column=0,padx=10,pady=10)
cuadroTexto6=Entry(miFrame)
cuadroTexto6.grid(row=7,column=1,padx=10,pady=10)
nombreLabel6=Label(miFrame, text='conductividad fluido tubo((BTU/h ft F)):')
nombreLabel6.grid(row=7,column=0,padx=10,pady=10)
cuadroTexto7=Entry(miFrame)
cuadroTexto7.grid(row=3,column=1,padx=10,pady=10)
nombreLabel7=Label(miFrame, text='conductividad fluido coraza((BTU/h ft F)):')
nombreLabel7.grid(row=3,column=0,padx=10,pady=10)
cuadroTexto8=Entry(miFrame)
cuadroTexto8.grid(row=8,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='masa del fluido del tubo (lb/h):')
nombreLabel8.grid(row=8,column=0,padx=10,pady=10)
cuadroTexto9=Entry(miFrame)
cuadroTexto9.grid(row=9,column=1,padx=10,pady=10)
nombreLabel9=Label(miFrame, text='masa del fluido dela coraza (lb/h):')
nombreLabel9.grid(row=9,column=0,padx=10,pady=10)
cuadroTexto10=Entry(miFrame)
cuadroTexto10.grid(row=10,column=1,padx=10,pady=10)
nombreLabel10=Label(miFrame, text='rd fluido tubo(lb/ft^3):') 
nombreLabel10.grid(row=10,column=0,padx=10,pady=10)
cuadroTexto11=Entry(miFrame)
cuadroTexto11.grid(row=11,column=1,padx=10,pady=10)
nombreLabel11=Label(miFrame, text='rd fluido coraza((F ft^2 h/ BTU)):')
nombreLabel11.grid(row=11,column=0,padx=10,pady=10)
cuadroTexto12=Entry(miFrame)
cuadroTexto12.grid(row=12,column=1,padx=10,pady=10)
nombreLabel12=Label(miFrame, text='temperatura 1 fluido tubo(°F):')
nombreLabel12.grid(row=12,column=0,padx=10,pady=10)
cuadroTexto13=Entry(miFrame)
cuadroTexto13.grid(row=13,column=1,padx=10,pady=10)
nombreLabel13=Label(miFrame, text='temperatura 2 fluido tubo(°F):')
nombreLabel13.grid(row=13,column=0,padx=10,pady=10)
cuadroTexto14=Entry(miFrame)
cuadroTexto14.grid(row=14,column=1,padx=10,pady=10)
nombreLabel14=Label(miFrame, text='temperatura 1 fluido coraza(°F):')
nombreLabel14.grid(row=14,column=0,padx=10,pady=10)
cuadroTexto15=Entry(miFrame)
cuadroTexto15.grid(row=15,column=1,padx=10,pady=10)
nombreLabel15=Label(miFrame, text='temperatura 2 fluido coraza(°F):')
nombreLabel15.grid(row=15,column=0,padx=10,pady=10)
cuadroTexto16=ttk.Combobox(miFrame,values=[
                                    "Coraza", 
                                    "Tubo",
                                    ],state="readonly")
cuadroTexto16.grid(row=16,column=1,padx=10,pady=10)
nombreLabel16=Label(miFrame, text='por donde ira el fluido caliente?:')
nombreLabel16.grid(row=16,column=0,padx=10,pady=10)
cuadroTexto17=Entry(miFrame)
cuadroTexto17.grid(row=17,column=1,padx=10,pady=10)
nombreLabel17=Label(miFrame, text='longitud del tubo(ft):')
nombreLabel17.grid(row=17,column=0,padx=10,pady=10)
cuadroTexto18=Entry(miFrame)
cuadroTexto18.grid(row=18,column=1,padx=10,pady=10)
nombreLabel18=Label(miFrame, text='rd externa(h*ft^2*°F/btu):')
nombreLabel18.grid(row=18,column=0,padx=10,pady=10)
cuadroTexto19=Entry(miFrame)
cuadroTexto19.grid(row=19,column=1,padx=10,pady=10)
nombreLabel19=Label(miFrame, text='longitud del anulo(ft):')
nombreLabel19.grid(row=19,column=0,padx=10,pady=10)
#----------------------------------------output grafico------------------------------------------------#
nombreLabel10=Label(miFrame, text="calorQ:")
nombreLabel10.grid(row=0,column=2,padx=10,pady=10)
nombreLabel11=Label(miFrame, textvariable=variabletexto)
nombreLabel11.grid(row=0,column=3,padx=10,pady=10)
nombreLabel12=Label(miFrame, text="lmtd:")
nombreLabel12.grid(row=1,column=2,padx=10,pady=10)
nombreLabel13=Label(miFrame, textvariable=lmtdtexto)
nombreLabel13.grid(row=1,column=3,padx=10,pady=10)
nombreLabel14=Label(miFrame, text="h int:")
nombreLabel14.grid(row=2,column=2,padx=10,pady=10)
nombreLabel15=Label(miFrame, textvariable=hinttexto)
nombreLabel15.grid(row=2,column=3,padx=10,pady=10)
nombreLabel16=Label(miFrame, text="h ext:")
nombreLabel16.grid(row=3,column=2,padx=10,pady=10)
nombreLabel17=Label(miFrame, textvariable=hexttexto)
nombreLabel17.grid(row=3,column=3,padx=10,pady=10)
nombreLabel18=Label(miFrame, text="u clean interna:")
nombreLabel18.grid(row=4,column=2,padx=10,pady=10)
nombreLabel19=Label(miFrame, textvariable=uclean1texto)
nombreLabel19.grid(row=4,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="u diseño  interna:")
nombreLabel20.grid(row=5,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=udiseno1texto)
nombreLabel21.grid(row=5,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="area transferencia interna:")
nombreLabel20.grid(row=6,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=areatrans1texto)
nombreLabel21.grid(row=6,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="numero de orquillas interna:")
nombreLabel20.grid(row=7,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=numerorq1texto)
nombreLabel21.grid(row=7,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="rdfinal interna:")
nombreLabel20.grid(row=8,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=rdfinal1texto)
nombreLabel21.grid(row=8,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="u clean externa:")
nombreLabel20.grid(row=9,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=uclean2texto)
nombreLabel21.grid(row=9,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="u diseño  externa:")
nombreLabel20.grid(row=10,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=udiseno2texto)
nombreLabel21.grid(row=10,column=3,padx=10,pady=10)
nombreLabel22=Label(miFrame, text="area transferencia externa:")
nombreLabel22.grid(row=11,column=2,padx=10,pady=10)
nombreLabel23=Label(miFrame, textvariable=areatrans2texto)
nombreLabel23.grid(row=11,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="numero orquillas externa:")
nombreLabel20.grid(row=12,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=numerorq2texto)
nombreLabel21.grid(row=12,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="rdfinal externa:")
nombreLabel20.grid(row=13,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=rdfinal2texto)
nombreLabel21.grid(row=13,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text="delta p:")
nombreLabel20.grid(row=14,column=2,padx=10,pady=10)
nombreLabel21=Label(miFrame, textvariable=deltaptexto)
nombreLabel21.grid(row=14,column=3,padx=10,pady=10)

#---------------funcion que llama el boton para calcular todo-----------#
def codigoBoton():
    # 1: tubo 
    # 2: coraza
    if(cuadroTexto0.get()==''):
        messagebox.showwarning('','la densidad del fluido del tubo no puede estar vacio')
        return None
    if(cuadroTexto1.get()==''):
        messagebox.showwarning('','la densidad del fluido de la coraza no puede estar vacio')
        return None
    densidad1 =float(cuadroTexto0.get())
    densidad2 = float(cuadroTexto1.get())
    #condicional para evitar que haya mas de uno vacio al tiempo
    if( (cuadroTexto8.get()=='' and cuadroTexto9.get()=='') or (cuadroTexto8.get()=='' and cuadroTexto12.get()=='') or (cuadroTexto8.get()=='' and cuadroTexto13.get()=='')or (cuadroTexto8.get()=='' and cuadroTexto14.get()=='') or(cuadroTexto8.get()=='' and  cuadroTexto15.get()=='') or(cuadroTexto9.get()=='' and cuadroTexto12.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto13.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto14.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto15.get()=='') or (cuadroTexto12.get()=='' and cuadroTexto13.get()=='') or (cuadroTexto12.get()=='' and cuadroTexto14.get()=='')or (cuadroTexto12.get()=='' and cuadroTexto15.get()=='')or (cuadroTexto13.get()=='' and cuadroTexto14.get()=='') or (cuadroTexto13.get()=='' and cuadroTexto15.get()=='') or (cuadroTexto14.get()=='' and cuadroTexto15.get()=='')):
        messagebox.showwarning('','no puede haber mas de una variable de temperaturas y masas vacia al tiempo')
        return None
    
    if(cuadroTexto2.get()==''):
        messagebox.showwarning('','el cp del fluido del tubo no puede estar vacio')
        return None
    if(cuadroTexto3.get()==''):
        messagebox.showwarning('','el cp del fluido de la coraza no puede estar vacio')
        return None
    if(cuadroTexto4.get()==''):
        messagebox.showwarning('','la viscodiad del fluido del tubo no puede estar vacio')
        return None
    if(cuadroTexto5.get()==''):
        messagebox.showwarning('','la viscosidad del fluido de la coraza no puede estar vacio')
        return None
    if(cuadroTexto6.get()==''):
        messagebox.showwarning('','la conductividad del fluido del tubo no puede estar vacio')
        return None
    if(cuadroTexto7.get()==''):
        messagebox.showwarning('','la conductividad del fluido de la coraza no puede estar vacio')
        return None
    if(cuadroTexto10.get()==''):
        messagebox.showwarning('','el rd del fluido del tubo no puede estar vacio pero si puede ser 0')
        return None
    if(cuadroTexto11.get()==''):
        messagebox.showwarning('','el rd del fluido de la coraza no puede estar vacio pero si puede ser 0')
        return None

    cp1 = float(cuadroTexto2.get())
    cp2 = float(cuadroTexto3.get())
    viscocidad1 = float(cuadroTexto4.get())
    viscocidad2 = float(cuadroTexto5.get())
    viscocidadft1 = viscocidad1 * 2.42
    viscocidadft2 = viscocidad2 * 2.42
    conductividad1 = float(cuadroTexto6.get())
    conductividad2 = float(cuadroTexto7.get())
    masa1 =0
    if(cuadroTexto8.get()==''):
        Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
        masa1=Q/abs(cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
    else:
        masa1=float(cuadroTexto8.get())
    
    masa2=0

    if(cuadroTexto9.get()==''):
        Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
        masa2=Q/abs(cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
    else:
        masa2=float(cuadroTexto9.get())
    TH1 = 0
    if(cuadroTexto12.get()==''):
        if(cuadroTexto16.get()=='Tubo'):
            Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
            TH1=float(cuadroTexto13.get())+(Q/(cp1*float(cuadroTexto8.get())))
        else:
            Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
            TH1=float(cuadroTexto13.get())-(Q/(cp1*float(cuadroTexto8.get())))
    else:
        TH1=float(cuadroTexto12.get())
    
    TH2 = 0
    if(cuadroTexto13.get()==''):
        if(cuadroTexto16.get()=='Tubo'):
            Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
            TH2=float(cuadroTexto12.get())-(Q/(cp1*float(cuadroTexto8.get())))
        else:
            Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
            TH2=float(cuadroTexto12.get())+(Q/(cp1*float(cuadroTexto8.get())))
    else:
        TH2=float(cuadroTexto13.get())
    
    tc1 = 0
    if(cuadroTexto14.get()==''):
        if(cuadroTexto16.get()=='Coraza'):
            Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
            tc1=float(cuadroTexto15.get())+(Q/(cp2*float(cuadroTexto9.get())))
        else:
            Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
            tc1=float(cuadroTexto15.get())-(Q/(cp2*float(cuadroTexto9.get())))
    else:
        tc1=float(cuadroTexto14.get())

    tc2 = 0

    if(cuadroTexto15.get()==''):
        if(cuadroTexto16.get()=='Coraza'):
            Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
            tc2=float(cuadroTexto14.get())-(Q/(cp2*float(cuadroTexto9.get())))
        else:
            Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
            tc2=float(cuadroTexto14.get())+(Q/(cp2*float(cuadroTexto9.get())))
    else:
        tc2=float(cuadroTexto15.get())
    rd1 = float(cuadroTexto10.get())
    rd2 = float(cuadroTexto11.get())
    
    
    
    
    temprom1 = (TH1 + TH2) / 2
    temprom2 = (tc1 + tc2) / 2

    # a) Calcular el calor
    Q = masa1 * cp1 * (TH1 - TH2)
    print(Q)
    variabletexto.set(str(Q))

    
    # b) Suponer un U de diseño de las tablas
    udiseño = 150
    #Suponer numero de pasos por los tubos
    lmtd = ((TH1-tc2)-(TH2-tc1))/math.log((TH1-tc2)/(TH2-tc1))
    R = (tc1-tc2)/(TH2-TH1)
    S = (TH2-TH1)/(tc1-TH1)
    F = ((math.sqrt((R**2)+1))*math.log((1-S)/(1-R*S)))/((R-1)*math.log((2-S*(R+1-math.sqrt((R**2)+1)))/(2-S*(R+1+math.sqrt((R**2)+1)))))
    area = Q/(lmtd*F*150)
    print(area)
    lmtd = lmtd * F

    # c) calculo de cantidad de tubos
    diamNominal = 3/4
    L = 14.0
    bwg = 10
    diamNominalstr = '3/4'
    diamintin = calcDiametro(diamNominalstr, str(bwg))
    diamintft = diamintin/12
    diamextft = diamNominal/12
    areatuboint = (math.pi*(diamintin**2))/4
    areatubointft = areatuboint/144
    vflujofts = 5
    vflujofth = vflujofts * 3600
    areaflujo = masa1/(densidad1*vflujofth)
    numTubos = math.ceil(areaflujo/areatubointft)
    print(numTubos)

    # d) calculo de cantidad de pasos
    areatransferenciain = math.pi*(diamintin*L)
    areatransferenciaft = areatransferenciain/12
    numPasos = math.ceil(area/(areatransferenciaft*numTubos))
    if(numPasos % 2 != 0):
        numPasos += 1
    print(numPasos)
    tubosTotales = numTubos * numPasos

    # e) recalculo del area de transferencia de calor
    area = numTubos * numPasos * math.pi * diamintft * L
    
    # f) recalculo el U de diseño
    udiseñocalc = Q/(area*lmtd)
    
    # g) coraza
    pitch = 1
    diamcorazain = 17 + (1/4)
    numBafles = math.ceil(2 * L * 0.3048)
    print(numBafles)
    rangomenor = diamcorazain/5
    b = (rangomenor+diamcorazain)/2
    print(b)

    # h) coeficiente de pelicula de la coraza
    dequivin = (4 * (pitch - (math.pi * (diamNominal**2))/4))/(math.pi*diamNominal)
    dequivft = dequivin/12
    clearance = pitch-diamNominal
    areaflujocorazain = (diamcorazain*clearance*b)/pitch
    areaflujocorazaft = areaflujocorazain/144
    gastoG = masa2/areaflujocorazaft
    
    # i) coeficiente de pelicula de los tubos
    reynolds2 = (dequivft*gastoG)/viscocidadft2
    prandt2 = (cp2 * viscocidadft2)/conductividad2
    nusell2 = 0.36 * ((reynolds2)**0.55)*((prandt2)**(1/3))
    if (viscocidad2 > 1):
        nusell2 *= (viscocidad2/1)**0.14
    hext = (nusell2*conductividad2)/dequivft
    print(hext)
    reynolds1 = (diamintft * masa1)/(areaflujo*viscocidadft1)
    prandt1 = cp1 * viscocidadft1 / conductividad1
    nusell1 = 0.027 * (reynolds1**0.8) * (prandt1**(1/3))
    if (viscocidad1 > 1):
        nusell1 *= (viscocidad1/1)**0.14
    hint = (nusell1*conductividad1)/diamintft
    print(hint)
    
    # j) Calcular el U de acuerdo a los h calculados
    divihi = 1/ hint
    divihext = 1/(hext * (diamextft / diamintft))
    rdint = 0.004
    rdext = 0
    udiseñocalc = 1/(divihi+divihext+rdint+rdext)
    print(udiseñocalc)
    uclean = 1/(divihi+divihext)
    print(uclean)
    porcentaje = (udiseño-udiseñocalc)/udiseño*100
    print(porcentaje)
    

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()