import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

raiz = Tk()#creacion interfaz

miFrame=Frame(raiz,width=1000,height=1000)#tamaño inicial

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
areatexto=StringVar()
ntubostexto=StringVar()
numpasostextos=StringVar()
numbaflestexto=StringVar()
btexto=StringVar()
npasostexto=StringVar()
hexttexto=StringVar()
hinttexto=StringVar()
disenocalctexto=StringVar()
ucleantexto=StringVar()
porcentajetexto=StringVar()
numerorq2texto=StringVar()
rdfinal2texto=StringVar()
deltaptexto=StringVar()
disenocalctexto_externo=StringVar()
ucleantexto_externo=StringVar()
Resistcondinterna_interna=StringVar()
Resistconvinterna_interna=StringVar()
Resistconvexterna_interna=StringVar()
Resistcondinterna_externa=StringVar()
Resistconvinterna_externa=StringVar()
Resistconvexterna_externa=StringVar()
masa1tex=StringVar()
masa2tex=StringVar()
tt1texto=StringVar()
tt2texto=StringVar()
tc1texto=StringVar()
tc2texto=StringVar()
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
cuadroTexto8=Entry(miFrame,textvariable=masa1tex)
cuadroTexto8.grid(row=8,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='masa del fluido del tubo (lb/h):')
nombreLabel8.grid(row=8,column=0,padx=10,pady=10)
cuadroTexto9=Entry(miFrame,textvariable=masa2tex)
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
cuadroTexto12=Entry(miFrame,textvariable=tt1texto)
cuadroTexto12.grid(row=12,column=1,padx=10,pady=10)
nombreLabel12=Label(miFrame, text='temperatura 1 fluido tubo(°F):')
nombreLabel12.grid(row=12,column=0,padx=10,pady=10)
cuadroTexto13=Entry(miFrame,textvariable=tt2texto)
cuadroTexto13.grid(row=13,column=1,padx=10,pady=10)
nombreLabel13=Label(miFrame, text='temperatura 2 fluido tubo(°F):')
nombreLabel13.grid(row=13,column=0,padx=10,pady=10)
cuadroTexto14=Entry(miFrame,textvariable=tc1texto)
cuadroTexto14.grid(row=14,column=1,padx=10,pady=10)
nombreLabel14=Label(miFrame, text='temperatura 1 fluido coraza(°F):')
nombreLabel14.grid(row=14,column=0,padx=10,pady=10)
cuadroTexto15=Entry(miFrame,textvariable=tc2texto)
cuadroTexto15.grid(row=15,column=1,padx=10,pady=10)
nombreLabel15=Label(miFrame, text='temperatura 2 fluido coraza(°F):')#hasta aqui se ve
nombreLabel15.grid(row=15,column=0,padx=10,pady=10)
cuadroTexto16=ttk.Combobox(miFrame,values=[
                                    "Coraza", 
                                    "Tubo",
                                    ],state="readonly")
cuadroTexto16.grid(row=6,column=3,padx=10,pady=10)
nombreLabel16=Label(miFrame, text='por donde ira el fluido caliente?:')
nombreLabel16.grid(row=6,column=2,padx=10,pady=10)
cuadroTexto17=Entry(miFrame)
cuadroTexto17.grid(row=7,column=3,padx=10,pady=10)
nombreLabel17=Label(miFrame, text='U diseño (BTU/h f ft^2) 100-200:')
nombreLabel17.grid(row=7,column=2,padx=10,pady=10)
cuadroTexto18=ttk.Combobox(miFrame,values=[
                                    "3/4", 
                                    "1",
                                    "1(1/4)"
                                    ],state="readonly")
cuadroTexto18.grid(row=8,column=3,padx=10,pady=10)
nombreLabel18=Label(miFrame, text='diametro nominal(in):')
nombreLabel18.grid(row=8,column=2,padx=10,pady=10)
cuadroTexto19=Entry(miFrame)
cuadroTexto19.grid(row=9,column=3,padx=10,pady=10)
nombreLabel19=Label(miFrame, text='valor de L (ft):')
nombreLabel19.grid(row=9,column=2,padx=10,pady=10)
cuadroTexto20=ttk.Combobox(miFrame,values=[
                                    "10", 
                                    "12",
                                    "14",
                                    "16"
                                    ],state="readonly")
cuadroTexto20.grid(row=0,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text='valor de  BWG:')
nombreLabel20.grid(row=0,column=2,padx=10,pady=10)
cuadroTexto21=Entry(miFrame)
cuadroTexto21.grid(row=1,column=3,padx=10,pady=10)
nombreLabel21=Label(miFrame, text='v flujo ( heuristico) (ft/s):')
nombreLabel21.grid(row=1,column=2,padx=10,pady=10)
cuadroTexto22=ttk.Combobox(miFrame,values=[
                                    "1,  3/4 triangular y cuadrado ", 
                                    "1.25 ,1 triangular y cuadrado ",
                                    "1.5625, 1 1/4triangular y cuadrado ",
                                    ],state="readonly")
cuadroTexto22.config(width=27)
cuadroTexto22.grid(row=2,column=3,padx=10,pady=10)
nombreLabel22=Label(miFrame, text='valor de  PITCH:')
nombreLabel22.grid(row=2,column=2,padx=10,pady=10)
cuadroTexto23=Entry(miFrame)
cuadroTexto23.grid(row=3,column=3,padx=10,pady=10)
nombreLabel23=Label(miFrame, text='Diametro coraza (in):')
nombreLabel23.grid(row=3,column=2,padx=10,pady=10)
cuadroTexto24=ttk.Combobox(miFrame,values=[
                                    "cuadrado", 
                                    "triangular",
                                    ],state="readonly")
cuadroTexto24.grid(row=4,column=3,padx=10,pady=10)
nombreLabel24=Label(miFrame, text='que tipo de arreglo es:')
nombreLabel24.grid(row=4,column=2,padx=10,pady=10)
cuadroTexto27=Entry(miFrame)
cuadroTexto27.grid(row=5,column=3,padx=10,pady=10)
nombreLabel27=Label(miFrame, text='K Conductividad del tubo (btu/ft*h*°F):')
nombreLabel27.grid(row=5,column=2,padx=10,pady=10)

#----------------------------------------output grafico------------------------------------------------#
nombreLabelo10=Label(miFrame, text="calorQ:")
nombreLabelo10.grid(row=0,column=4,padx=10,pady=10)
nombreLabelo11=Label(miFrame, textvariable=variabletexto)
nombreLabelo11.grid(row=0,column=5,padx=10,pady=10)
nombreLabelo12=Label(miFrame, text="area:")
nombreLabelo12.grid(row=1,column=4,padx=10,pady=10)
nombreLabelo13=Label(miFrame, textvariable=areatexto)
nombreLabelo13.grid(row=1,column=5,padx=10,pady=10)
nombreLabelo14=Label(miFrame, text="numero tubos:")
nombreLabelo14.grid(row=2,column=4,padx=10,pady=10)
nombreLabelo15=Label(miFrame, textvariable=ntubostexto)
nombreLabelo15.grid(row=2,column=5,padx=10,pady=10)
nombreLabelo16=Label(miFrame, text="numero de pasos:")
nombreLabelo16.grid(row=3,column=4,padx=10,pady=10)
nombreLabelo17=Label(miFrame, textvariable=numpasostextos)
nombreLabelo17.grid(row=3,column=5,padx=10,pady=10)
nombreLabelo18=Label(miFrame, text="numero de baffles:")
nombreLabelo18.grid(row=4,column=4,padx=10,pady=10)
nombreLabelo19=Label(miFrame, textvariable=numbaflestexto)
nombreLabelo19.grid(row=4,column=5,padx=10,pady=10)
nombreLabelo20=Label(miFrame, text="b escogido por uno:")
nombreLabelo20.grid(row=5,column=4,padx=10,pady=10)
nombreLabelo21=Label(miFrame, textvariable=btexto)
nombreLabelo21.grid(row=5,column=5,padx=10,pady=10)
nombreLabelo22=Label(miFrame, text="TUBOS TOTALES en n pasos:")
nombreLabelo22.grid(row=6,column=4,padx=10,pady=10)
nombreLabelo23=Label(miFrame, textvariable=npasostexto)
nombreLabelo23.grid(row=6,column=5,padx=10,pady=10)
nombreLabelo24=Label(miFrame, text="h externo coraza:")
nombreLabelo24.grid(row=7,column=4,padx=10,pady=10)
nombreLabelo25=Label(miFrame, textvariable=hexttexto)
nombreLabelo25.grid(row=7,column=5,padx=10,pady=10)
nombreLabelo26=Label(miFrame, text="h interno tubo:")
nombreLabelo26.grid(row=8,column=4,padx=10,pady=10)
nombreLabelo27=Label(miFrame, textvariable=hinttexto)
nombreLabelo27.grid(row=8,column=5,padx=10,pady=10)
nombreLabelo28=Label(miFrame, text="U diseño interno:")
nombreLabelo28.grid(row=9,column=4,padx=10,pady=10)
nombreLabelo29=Label(miFrame, textvariable=disenocalctexto)
nombreLabelo29.grid(row=9,column=5,padx=10,pady=10)
nombreLabelo30=Label(miFrame, text="u clean interno:")
nombreLabelo30.grid(row=10,column=4,padx=10,pady=10)
nombreLabelo31=Label(miFrame, textvariable=ucleantexto)
nombreLabelo31.grid(row=10,column=5,padx=10,pady=10)

nombreLabelo32=Label(miFrame, text="U diseño externo:")
nombreLabelo32.grid(row=11,column=4,padx=10,pady=10)
nombreLabelo33=Label(miFrame, textvariable=disenocalctexto_externo)
nombreLabelo33.grid(row=11,column=5,padx=10,pady=10)
nombreLabelo34=Label(miFrame, text="u clean externo:")
nombreLabelo34.grid(row=12,column=4,padx=10,pady=10)
nombreLabelo35=Label(miFrame, textvariable=ucleantexto_externo)
nombreLabelo35.grid(row=12,column=5,padx=10,pady=10)

nombreLabelo36=Label(miFrame, text="porcentaje entre los U:")
nombreLabelo36.grid(row=13,column=4,padx=10,pady=10)
nombreLabelo37=Label(miFrame, textvariable=porcentajetexto)
nombreLabelo37.grid(row=13,column=5,padx=10,pady=10)

nombreLabelo38=Label(miFrame, text="R cond in interno:")
nombreLabelo38.grid(row=14,column=4,padx=10,pady=10)
nombreLabelo39=Label(miFrame, textvariable=Resistcondinterna_interna)
nombreLabelo39.grid(row=14,column=5,padx=10,pady=10)
nombreLabelo40=Label(miFrame, text="R conv in interno:")#hasta aqui
nombreLabelo40.grid(row=15,column=4,padx=10,pady=10)
nombreLabelo41=Label(miFrame, textvariable=Resistconvinterna_interna)
nombreLabelo41.grid(row=15,column=5,padx=10,pady=10)
nombreLabelo42=Label(miFrame, text="R conv ex interno:")
nombreLabelo42.grid(row=0,column=6,padx=10,pady=10)
nombreLabelo43=Label(miFrame, textvariable=Resistconvexterna_interna)
nombreLabelo43.grid(row=0,column=7,padx=10,pady=10)
nombreLabelo44=Label(miFrame, text="R cond in externo:")
nombreLabelo44.grid(row=1,column=6,padx=10,pady=10)
nombreLabelo45=Label(miFrame, textvariable=Resistcondinterna_externa)
nombreLabelo45.grid(row=1,column=7,padx=10,pady=10)
nombreLabelo46=Label(miFrame, text="R conv in externo:")
nombreLabelo46.grid(row=2,column=6,padx=10,pady=10)
nombreLabelo47=Label(miFrame, textvariable=Resistconvinterna_externa)
nombreLabelo47.grid(row=2,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="R conv ex externo:")
nombreLabelo48.grid(row=3,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Resistconvexterna_externa)
nombreLabelo49.grid(row=3,column=7,padx=10,pady=10)

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
    
    masa1tex.set(str(masa1))
    masa2=0

    if(cuadroTexto9.get()==''):
        Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto12.get())-float(cuadroTexto13.get())))
        masa2=Q/abs(cp2*(float(cuadroTexto14.get())-float(cuadroTexto15.get())))
    else:
        masa2=float(cuadroTexto9.get())
    masa2tex.set(str(masa2))
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
    tt1texto.set(str(TH1))
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
    tt2texto.set(str(TH2))
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
    tc1texto.set(tc1)
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
    
    tc2texto.set(str(tc2))
    rd1 = float(cuadroTexto10.get())
    rd2 = float(cuadroTexto11.get())
    
    
    
    
    temprom1 = (TH1 + TH2) / 2
    temprom2 = (tc1 + tc2) / 2

    # a) Calcular el calor
    Q = masa1 * cp1 * (TH1 - TH2)
    print(Q)
    variabletexto.set(str(Q))

    if(cuadroTexto17.get()==''):
        messagebox.showwarning('','el u de diseño no puede estar vacio pero si puede ser un valor de 100 a 200')
        return None
    
    if(float(cuadroTexto17.get())>200 or float(cuadroTexto17.get())<100):
        messagebox.showwarning('','el u de diseño debe ser un valor de 100 a 200')
        return None
    # b) Suponer un U de diseño de las tablas
    udiseno = float(cuadroTexto17.get())
    #Suponer numero de pasos por los tubos
    if(math.log((TH1-tc2)/(TH2-tc1))<=0):
        lmtd= (TH1-tc2)+(TH2-tc1)/2
    else:
        lmtd = ((TH1-tc2)-(TH2-tc1))/math.log((TH1-tc2)/(TH2-tc1))
    
    R = (tc1-tc2)/(TH2-TH1)
    S = (TH2-TH1)/(tc1-TH1)
    F = ((math.sqrt((R**2)+1))*math.log((1-S)/(1-R*S)))/((R-1)*math.log((2-S*(R+1-math.sqrt((R**2)+1)))/(2-S*(R+1+math.sqrt((R**2)+1)))))
    if(F<0.75):
        messagebox.showwarning('','F da un valor menor a 0.75')
        return None
    area = Q/(lmtd*F*udiseno)
    print(area)
    areatexto.set(str(area))
    lmtd = lmtd * F

    # c) calculo de cantidad de tubos
    if(cuadroTexto18.get()==''):
        messagebox.showwarning('','el diametro nominal no puede estar vacio')
        return None
    diamNominal = 0
    if(cuadroTexto18.get()=="3/4"):
        diamNominal=0.75
    elif(cuadroTexto18.get()=="1"):
        diamNominal=1
    elif(cuadroTexto18.get()=="1 1/4"):
        diamNominal=1.25
    if(cuadroTexto19.get()==''):
        messagebox.showwarning('','el L no puede estar vacio pero si puede ser un valor de 8 y 36')
        return None
    L = float(cuadroTexto19.get())
    if(cuadroTexto20.get()==''):
        messagebox.showwarning('','el bwg no puede estar vacio')
        return None
    bwg = cuadroTexto20.get()
    diamNominalstr = cuadroTexto18.get()
    diamintin = calcDiametro(diamNominalstr, bwg)
    diamintft = diamintin/12
    diamextft = diamNominal/12
    areatuboint = (math.pi*(diamintin**2))/4
    areatubointft = areatuboint/144
    if(cuadroTexto21.get()==''):
        messagebox.showwarning('','el diametro nominal no puede estar vacio pero si puede ser un valor de 100 a 200')
        return None
    vflujofts = float(cuadroTexto21.get())
    vflujofth = vflujofts * 3600
    areaflujo = masa1/(densidad1*vflujofth)
    numTubos = math.ceil(areaflujo/areatubointft)
    print(numTubos)
    ntubostexto.set(str(numTubos))

    # d) calculo de cantidad de pasos
    areatransferenciain = math.pi*(diamintin*L)
    areatransferenciaft = areatransferenciain/12
    numPasos = math.ceil(area/(areatransferenciaft*numTubos))
    if(numPasos % 2 != 0):
        numPasos += 1
    print(numPasos)
    numpasostextos.set(str(numPasos))

    tubosTotales = numTubos * numPasos
    print(tubosTotales)

    npasostexto.set(str(tubosTotales))

    # e) recalculo del area de transferencia de calor
    area = numTubos * numPasos * math.pi * diamintft * L
    
    # f) recalculo el U de diseño
    udiseñocalc_interno = Q/(area*lmtd)
    
    # g) coraza
    if(cuadroTexto22.get()==''):
        messagebox.showwarning('','el PITCH no puede estar vacio')
        return None
    pitch = 0
    if(cuadroTexto22.get()=='1,  3/4 triangular y cuadrado '):
        pitch=1
    elif(cuadroTexto22.get()=='1.25 ,1 triangular y cuadrado '):
        pitch=1.25
    elif(cuadroTexto22.get()=='1.5625, 1 1/4triangular y cuadrado '):
        pitch=1.5625
    
    if(cuadroTexto23.get()==''):
        messagebox.showwarning('','el diametro coraza no puede estar vacio')
        return None

    diamcorazain = float(cuadroTexto23.get())
    numBafles = math.ceil(2 * L * 0.3048)
    print(numBafles)
    numbaflestexto.set(str(numBafles))
    rangomenor = diamcorazain/5
    b = (rangomenor+diamcorazain)/2
    print(b)
    btexto.set(str(b))

    # h) coeficiente de pelicula de la coraza
    dequivin=0
    if(cuadroTexto24.get()==''):
        messagebox.showwarning('','el tipo de arreglo no puede estar vacio ')
        return None
    if(cuadroTexto24.get()=="cuadrado"):
        dequivin = (4 * (pitch - (math.pi * (diamNominal**2))/4))/(math.pi*diamNominal)
    else:
        dequivin=(4 * 1/2*pitch*0.86*pitch - 0.5*math.pi * (diamNominal**2/4))/(1/2*math.pi*diamNominal)
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
    hextc = (nusell2*conductividad2)/dequivft
    print(hextc)
    hexttexto.set(str(hextc))

    reynolds1 = (diamintft * masa1)/(areaflujo*viscocidadft1)
    prandt1 = cp1 * viscocidadft1 / conductividad1
    nusell1 = 0.027 * (reynolds1**0.8) * (prandt1**(1/3))
    if (viscocidad1 > 1):
        nusell1 *= (viscocidad1/1)**0.14
    hint = (nusell1*conductividad1)/diamintft
    print(hint)
    hinttexto.set(str(hint))
    
    # j) Calcular el U de acuerdo a los h calculados
    divihi_interno = 1/ hint
    divihextc_interno = 1/(hextc * (diamextft / diamintft))
    
    
    if(cuadroTexto27.get()==''):
        messagebox.showwarning('','el campo conductividad del tubo no puede estar vacio ')
        return None
    
    k_conductividad_tubo=float(cuadroTexto27.get())
    rdint_interno = rd1
    rdext_interno = rd2
    logaritmo_para_despues1=(math.log(diamextft/diamintft)*diamintft)/(2*k_conductividad_tubo)

    Resistcondinterna_externa.set(str(logaritmo_para_despues1))
    Resistcondinterna_interna.set(str(logaritmo_para_despues1))
    Resistconvinterna_interna.set(str(divihi_interno))
    Resistconvexterna_interna.set(str(divihextc_interno))

    udiseñocalc_interno = 1/(divihi_interno+divihextc_interno+rdint_interno+rdext_interno*(diamintft/diamextft)+logaritmo_para_despues1)
    print(udiseñocalc_interno)
    disenocalctexto.set(str(udiseñocalc_interno))
    uclean_interno = 1/(divihi_interno+divihextc_interno)
    print(uclean_interno)
    ucleantexto.set(str(uclean_interno))


    divihi_externo = 1/ (hint*diamintft/diamextft)
    divihextc_externo = 1/hextc

    Resistconvinterna_externa.set(str(divihi_externo))
    Resistconvexterna_externa.set(str(divihextc_externo))

    rdint_externo = rd1
    rdext_externo = rd2
    udiseñocalc_externo = 1/(divihi_externo+divihextc_externo+rdext_externo+rdint_externo*(diamextft/diamintft)+logaritmo_para_despues1)
    print(udiseñocalc_externo)
    disenocalctexto_externo.set(str(udiseñocalc_externo))
    uclean_externo = 1/(divihi_externo+divihextc_externo)
    print(uclean_externo)
    ucleantexto_externo.set(str(uclean_externo))
    porcentaje = (udiseno-udiseñocalc_interno)/udiseno*100
    print(porcentaje)
    porcentajetexto.set(str(porcentaje))
    win1 = Toplevel()
    win1.wm_title("Tabla1")
    tabla1=ImageTk.PhotoImage(Image.open("Tabla_cuadrada.png"))
    Label1=Label(win1,image=tabla1)
    Label1.image= tabla1
    Label1.pack()
    win2 = Toplevel()
    win2.wm_title("Tabla2")
    tabla2=ImageTk.PhotoImage(Image.open("Tabla_triangular.png"))
    Label2=Label(win2,image=tabla2)
    Label2.image=tabla2
    Label2.pack()
    print('x')
    

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()