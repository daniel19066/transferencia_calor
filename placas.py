import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
#Holiii
raiz = Tk()#creacion interfaz

miFrame=Frame(raiz)#tamaño inicial

miFrame.pack(fill=BOTH,expand=1)
win1 = Toplevel()
win1.wm_title("imagen guia")
tabla1=ImageTk.PhotoImage(Image.open("placas.png"))
Label1=Label(win1,image=tabla1)
Label1.image= tabla1
Label1.pack()


#Funcion para calcular el diametro interno y externo en Cedula 40
def calcCheviron(cheviron, reynolds):
    if cheviron == 30:
        if(reynolds < 10):
            ch = 0.718
            n = 0.349
            kp = 50
            m = 1
        if(reynolds > 10):
            ch = 0.348 
            n = 0.663
        if(reynolds > 10 and reynolds < 100):
            kp = 19.4
            m = 0.589
        elif(reynolds > 100):
            kp = 2.99
            m = 0.183
    elif cheviron == 45:
        if (reynolds < 10):
            ch = 0.718
            n = 0.349
        elif (reynolds > 10 and reynolds < 100):
            ch = 0.4
            n = 0.598
        elif (reynolds > 100):
            ch = 0.3
            n = 0.663
        if(reynolds < 15):
            kp = 47
            m = 1
        if(reynolds > 15 and reynolds < 300):
            kp = 18.29
            m = 0.652
        if(reynolds > 300):
            kp = 1.441
            m = 0.206
    elif cheviron == 60:
        if(reynolds < 20):
            ch = 0.562
            n = 0.326
        elif(reynolds > 20 and reynolds < 400):
            ch = 0.306
            n = 0.529
        if(reynolds > 400):
            ch = 0.108
            n = 0.703
            kp = 0.639
            m = 0.215
        if(reynolds < 40):
            kp = 24
            m = 1
        elif(reynolds > 40 and reynolds < 400):
            kp = 2.8
            m = 0.457

    return ch, n, kp, m
#-------------------------------------------parte de la interfaz grafica-----------------------------------#

#--------------------------------------input-----------------------------------------------------#
variabletexto=StringVar()
reynolds1texto=StringVar()
prandtl1texto=StringVar()
reynolds2texto=StringVar()
prandtl2texto=StringVar()
lptextos=StringVar()
anchotexto=StringVar()
dptexto=StringVar()
factortexto=StringVar()
espaciadotexto=StringVar()
pitchtexto=StringVar()
espesortexto=StringVar()
placasutexto=StringVar()
Dhtexto=StringVar()
nussellhtexto=StringVar()
hcalientetexto=StringVar()
nussellctexto=StringVar()
hfriotexto=StringVar()
uctexto=StringVar()
udtexto=StringVar()
Cftexto=StringVar()
Qcleantexto=StringVar()
Qdisenotexto=StringVar()
Cstexto=StringVar()
fhottexto=StringVar()
fcoldtexto=StringVar()
Deltapchtexto=StringVar()
Deltapcctexto=StringVar()
Deltapphtexto=StringVar()
Deltappctexto=StringVar()
Deltapthtexto=StringVar()
Deltaptctexto=StringVar()

masa1tex=StringVar()
masa2tex=StringVar()
th1texto=StringVar()
th2texto=StringVar()
tc1texto=StringVar()
tc2texto=StringVar()
cuadroTexto0=Entry(miFrame)
cuadroTexto0.grid(row=0,column=1,padx=10,pady=10)
nombreLabel0=Label(miFrame, text='densidad fluido caliente(lb/ft^3):')
nombreLabel0.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=1,column=1,padx=10,pady=10)
nombreLabel1=Label(miFrame, text='densidad fluido frio(lb/ft^3):')
nombreLabel1.grid(row=1,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=2,column=1,padx=10,pady=10)
nombreLabel2=Label(miFrame, text='cp del fluido caliente(btu/lb°F):')
nombreLabel2.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=4,column=1,padx=10,pady=10)
nombreLabel3=Label(miFrame, text='cp del fluido frio(btu/lb°F):')
nombreLabel3.grid(row=4,column=0,padx=10,pady=10)
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=5,column=1,padx=10,pady=10)
nombreLabel4=Label(miFrame, text='viscosidad fluido caliente(cp):')
nombreLabel4.grid(row=5,column=0,padx=10,pady=10)
cuadroTexto5=Entry(miFrame)
cuadroTexto5.grid(row=6,column=1,padx=10,pady=10)
nombreLabel5=Label(miFrame, text='viscosidad fluido frio(cp):')
nombreLabel5.grid(row=6,column=0,padx=10,pady=10)
cuadroTexto6=Entry(miFrame)
cuadroTexto6.grid(row=7,column=1,padx=10,pady=10)
nombreLabel6=Label(miFrame, text='conductividad fluido caliente(W/m*K):')
nombreLabel6.grid(row=7,column=0,padx=10,pady=10)
cuadroTexto7=Entry(miFrame)
cuadroTexto7.grid(row=3,column=1,padx=10,pady=10)
nombreLabel7=Label(miFrame, text='conductividad fluido frio (W/m*K):')
nombreLabel7.grid(row=3,column=0,padx=10,pady=10)
cuadroTexto8=Entry(miFrame,textvariable=masa1tex)
cuadroTexto8.grid(row=8,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='masa del fluido caliente(lb/h):')
nombreLabel8.grid(row=8,column=0,padx=10,pady=10)
cuadroTexto9=Entry(miFrame,textvariable=masa2tex)
cuadroTexto9.grid(row=9,column=1,padx=10,pady=10)
nombreLabel9=Label(miFrame, text='masa del fluido frio(lb/h):')
nombreLabel9.grid(row=9,column=0,padx=10,pady=10)
cuadroTexto10=Entry(miFrame)
cuadroTexto10.grid(row=10,column=1,padx=10,pady=10)
nombreLabel10=Label(miFrame, text='rd fluido caliente(lb/ft^3):') 
nombreLabel10.grid(row=10,column=0,padx=10,pady=10)
cuadroTexto11=Entry(miFrame)
cuadroTexto11.grid(row=11,column=1,padx=10,pady=10)
nombreLabel11=Label(miFrame, text='rd fluido frio(m^2K/W):')
nombreLabel11.grid(row=11,column=0,padx=10,pady=10)
cuadroTexto12=Entry(miFrame,textvariable=th1texto)
cuadroTexto12.grid(row=12,column=1,padx=10,pady=10)
nombreLabel12=Label(miFrame, text='temperatura 1 fluido caliente(°F):')
nombreLabel12.grid(row=12,column=0,padx=10,pady=10)
cuadroTexto13=Entry(miFrame,textvariable=th2texto)
cuadroTexto13.grid(row=13,column=1,padx=10,pady=10)
nombreLabel13=Label(miFrame, text='temperatura 2 fluido caliente(°F):')
nombreLabel13.grid(row=13,column=0,padx=10,pady=10)
cuadroTexto14=Entry(miFrame,textvariable=tc1texto)
cuadroTexto14.grid(row=14,column=1,padx=10,pady=10)
nombreLabel14=Label(miFrame, text='temperatura 1 fluido frio(°F):')
nombreLabel14.grid(row=14,column=0,padx=10,pady=10)
cuadroTexto15=Entry(miFrame,textvariable=tc2texto)
cuadroTexto15.grid(row=15,column=1,padx=10,pady=10)
nombreLabel15=Label(miFrame, text='temperatura 2 fluido frio(°F):')
nombreLabel15.grid(row=15,column=0,padx=10,pady=10)
cuadroTexto17=Entry(miFrame)
cuadroTexto17.grid(row=7,column=3,padx=10,pady=10)
nombreLabel17=Label(miFrame, text='conductividad plato(W/m*K)(Kw):')
nombreLabel17.grid(row=7,column=2,padx=10,pady=10)
cuadroTexto18=Entry(miFrame)
cuadroTexto18.grid(row=8,column=3,padx=10,pady=10)
nombreLabel18=Label(miFrame, text='Lc plato(m):')
nombreLabel18.grid(row=8,column=2,padx=10,pady=10)
cuadroTexto19=Entry(miFrame)
cuadroTexto19.grid(row=9,column=3,padx=10,pady=10)
nombreLabel19=Label(miFrame, text='Lv plato(m):')
nombreLabel19.grid(row=9,column=2,padx=10,pady=10)
cuadroTexto20=Entry(miFrame)
cuadroTexto20.grid(row=0,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text='Lh plato (m):')
nombreLabel20.grid(row=0,column=2,padx=10,pady=10)
cuadroTexto21=Entry(miFrame)
cuadroTexto21.grid(row=1,column=3,padx=10,pady=10)
nombreLabel21=Label(miFrame, text='Dp plato(mm):')
nombreLabel21.grid(row=1,column=2,padx=10,pady=10)
cuadroTexto23=Entry(miFrame)
cuadroTexto23.grid(row=2,column=3,padx=10,pady=10)
nombreLabel23=Label(miFrame, text='espesor plato(mm):')
nombreLabel23.grid(row=2,column=2,padx=10,pady=10)
cuadroTexto24=ttk.Combobox(miFrame,values=[
                                    "30", 
                                    "45",
                                    "60"
                                    ],state="readonly")
cuadroTexto24.grid(row=3,column=3,padx=10,pady=10)
nombreLabel24=Label(miFrame, text='cheviron:')
nombreLabel24.grid(row=3,column=2,padx=10,pady=10)
cuadroTexto25=Entry(miFrame)
cuadroTexto25.grid(row=4,column=3,padx=10,pady=10)
nombreLabel25=Label(miFrame, text='numero placas plato:')
nombreLabel25.grid(row=4,column=2,padx=10,pady=10)
cuadroTexto26=Entry(miFrame)
cuadroTexto26.grid(row=5,column=3,padx=10,pady=10)
nombreLabel26=Label(miFrame, text='Area efectiva (m^2):')
nombreLabel26.grid(row=5,column=2,padx=10,pady=10)
cuadroTexto27=Entry(miFrame)
cuadroTexto27.grid(row=6,column=3,padx=10,pady=10)
nombreLabel27=Label(miFrame, text='numeor de pasos:')
nombreLabel27.grid(row=6,column=2,padx=10,pady=10)

#----------------------------------------output grafico------------------------------------------------#
nombreLabelo10=Label(miFrame, text="calorQ(W):")
nombreLabelo10.grid(row=0,column=4,padx=10,pady=10)
nombreLabelo11=Label(miFrame, textvariable=variabletexto)
nombreLabelo11.grid(row=0,column=5,padx=10,pady=10)
nombreLabelo12=Label(miFrame, text="reynolds caliente:")
nombreLabelo12.grid(row=1,column=4,padx=10,pady=10)
nombreLabelo13=Label(miFrame, textvariable=reynolds1texto)
nombreLabelo13.grid(row=1,column=5,padx=10,pady=10)
nombreLabelo14=Label(miFrame, text="prandtl caliente:")
nombreLabelo14.grid(row=2,column=4,padx=10,pady=10)
nombreLabelo15=Label(miFrame, textvariable=prandtl1texto)
nombreLabelo15.grid(row=2,column=5,padx=10,pady=10)
nombreLabelo12=Label(miFrame, text="reynolds frio:")
nombreLabelo12.grid(row=14,column=6,padx=10,pady=10)
nombreLabelo13=Label(miFrame, textvariable=reynolds2texto)
nombreLabelo13.grid(row=14,column=7,padx=10,pady=10)
nombreLabelo14=Label(miFrame, text="prandtl frio:")
nombreLabelo14.grid(row=15,column=6,padx=10,pady=10)
nombreLabelo15=Label(miFrame, textvariable=prandtl2texto)
nombreLabelo15.grid(row=15,column=7,padx=10,pady=10)
nombreLabelo16=Label(miFrame, text="longitud plato proyectada(m):")
nombreLabelo16.grid(row=3,column=4,padx=10,pady=10)
nombreLabelo17=Label(miFrame, textvariable=lptextos)
nombreLabelo17.grid(row=3,column=5,padx=10,pady=10)
nombreLabelo18=Label(miFrame, text="ancho de placa(m):")
nombreLabelo18.grid(row=4,column=4,padx=10,pady=10)
nombreLabelo19=Label(miFrame, textvariable=anchotexto)
nombreLabelo19.grid(row=4,column=5,padx=10,pady=10)
nombreLabelo20=Label(miFrame, text="diametro port(m):")
nombreLabelo20.grid(row=5,column=4,padx=10,pady=10)
nombreLabelo21=Label(miFrame, textvariable=dptexto)
nombreLabelo21.grid(row=5,column=5,padx=10,pady=10)
nombreLabelo22=Label(miFrame, text="factor ampliacion:")
nombreLabelo22.grid(row=6,column=4,padx=10,pady=10)
nombreLabelo23=Label(miFrame, textvariable=factortexto)
nombreLabelo23.grid(row=6,column=5,padx=10,pady=10)
nombreLabelo24=Label(miFrame, text="espaciado plato(m):")
nombreLabelo24.grid(row=7,column=4,padx=10,pady=10)
nombreLabelo25=Label(miFrame, textvariable=espaciadotexto)
nombreLabelo25.grid(row=7,column=5,padx=10,pady=10)
nombreLabelo26=Label(miFrame, text="pitch plato(m):")
nombreLabelo26.grid(row=8,column=4,padx=10,pady=10)
nombreLabelo27=Label(miFrame, textvariable=pitchtexto)
nombreLabelo27.grid(row=8,column=5,padx=10,pady=10)
nombreLabelo28=Label(miFrame, text="espesor(m):")
nombreLabelo28.grid(row=9,column=4,padx=10,pady=10)
nombreLabelo29=Label(miFrame, textvariable=espesortexto)
nombreLabelo29.grid(row=9,column=5,padx=10,pady=10)
nombreLabelo30=Label(miFrame, text="numero de placas utiles:")
nombreLabelo30.grid(row=10,column=4,padx=10,pady=10)
nombreLabelo31=Label(miFrame, textvariable=placasutexto)
nombreLabelo31.grid(row=10,column=5,padx=10,pady=10)

nombreLabelo32=Label(miFrame, text="Dh:")
nombreLabelo32.grid(row=11,column=4,padx=10,pady=10)
nombreLabelo33=Label(miFrame, textvariable=Dhtexto)
nombreLabelo33.grid(row=11,column=5,padx=10,pady=10)
nombreLabelo34=Label(miFrame, text="Nussel caliente:")
nombreLabelo34.grid(row=12,column=4,padx=10,pady=10)
nombreLabelo35=Label(miFrame, textvariable=nussellhtexto)
nombreLabelo35.grid(row=12,column=5,padx=10,pady=10)

nombreLabelo36=Label(miFrame, text="h, caliente:")
nombreLabelo36.grid(row=13,column=4,padx=10,pady=10)
nombreLabelo37=Label(miFrame, textvariable=hcalientetexto)
nombreLabelo37.grid(row=13,column=5,padx=10,pady=10)

nombreLabelo38=Label(miFrame, text="Nussell frio:")
nombreLabelo38.grid(row=14,column=4,padx=10,pady=10)
nombreLabelo39=Label(miFrame, textvariable=nussellctexto)
nombreLabelo39.grid(row=14,column=5,padx=10,pady=10)
nombreLabelo40=Label(miFrame, text="h,frio:")
nombreLabelo40.grid(row=15,column=4,padx=10,pady=10)
nombreLabelo41=Label(miFrame, textvariable=hfriotexto)
nombreLabelo41.grid(row=15,column=5,padx=10,pady=10)
nombreLabelo42=Label(miFrame, text="Uc:")
nombreLabelo42.grid(row=0,column=6,padx=10,pady=10)
nombreLabelo43=Label(miFrame, textvariable=uctexto)
nombreLabelo43.grid(row=0,column=7,padx=10,pady=10)
nombreLabelo44=Label(miFrame, text="Ud:")
nombreLabelo44.grid(row=1,column=6,padx=10,pady=10)
nombreLabelo45=Label(miFrame, textvariable=udtexto)
nombreLabelo45.grid(row=1,column=7,padx=10,pady=10)
nombreLabelo46=Label(miFrame, text="Cf:")
nombreLabelo46.grid(row=2,column=6,padx=10,pady=10)
nombreLabelo47=Label(miFrame, textvariable=Cftexto)
nombreLabelo47.grid(row=2,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Qclean(kw):")
nombreLabelo48.grid(row=3,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Qcleantexto)
nombreLabelo49.grid(row=3,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Qdiseño(kw):")
nombreLabelo48.grid(row=4,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Qdisenotexto)
nombreLabelo49.grid(row=4,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Cs:")
nombreLabelo48.grid(row=5,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Cstexto)
nombreLabelo49.grid(row=5,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="f hot:")
nombreLabelo48.grid(row=6,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=fhottexto)
nombreLabelo49.grid(row=6,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="f cold:")
nombreLabelo48.grid(row=7,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=fcoldtexto)
nombreLabelo49.grid(row=7,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Delta pc hot(psi):")
nombreLabelo48.grid(row=8,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltapchtexto)
nombreLabelo49.grid(row=8,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Delta pc cold(psi):")
nombreLabelo48.grid(row=9,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltapcctexto)
nombreLabelo49.grid(row=9,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Delta pp hot(psi):")
nombreLabelo48.grid(row=10,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltapphtexto)
nombreLabelo49.grid(row=10,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Delta pp cold (psi):")
nombreLabelo48.grid(row=11,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltappctexto)
nombreLabelo49.grid(row=11,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Deltapt hot(psi):")
nombreLabelo48.grid(row=12,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltapthtexto)
nombreLabelo49.grid(row=12,column=7,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="Deltapt cold(psi):")
nombreLabelo48.grid(row=13,column=6,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Deltaptctexto)
nombreLabelo49.grid(row=13,column=7,padx=10,pady=10)

#---------------funcion que llama el boton para calcular todo-----------#
def codigoBoton():

    #Tabla fluidos
    masa2 = 0
    if(cuadroTexto2.get()==''):
        messagebox.showwarning('','el cp del fluido caliente no puede estar vacio')
        return None
    if(cuadroTexto3.get()==''):
        messagebox.showwarning('','el cp del fluido frio no puede estar vacio')
        return None
    cp1 = float(cuadroTexto2.get())
    cp2 = float(cuadroTexto3.get())
    th1 = 0
    th2 = 0
    tc1 = 0
    tc2 = 0
     #condicional para evitar que haya mas de uno vacio al tiempo
    if( (cuadroTexto8.get()=='' and cuadroTexto9.get()=='') or (cuadroTexto8.get()=='' and cuadroTexto12.get()=='') or (cuadroTexto8.get()=='' and cuadroTexto13.get()=='')or (cuadroTexto8.get()=='' and cuadroTexto14.get()=='') or(cuadroTexto8.get()=='' and  cuadroTexto15.get()=='') or(cuadroTexto9.get()=='' and cuadroTexto12.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto13.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto14.get()=='') or (cuadroTexto9.get()=='' and cuadroTexto15.get()=='') or (cuadroTexto12.get()=='' and cuadroTexto13.get()=='') or (cuadroTexto12.get()=='' and cuadroTexto14.get()=='')or (cuadroTexto12.get()=='' and cuadroTexto15.get()=='')or (cuadroTexto13.get()=='' and cuadroTexto14.get()=='') or (cuadroTexto13.get()=='' and cuadroTexto15.get()=='') or (cuadroTexto14.get()=='' and cuadroTexto15.get()=='')):
        messagebox.showwarning('','no puede haber mas de una variable de temperaturas y masas vacia al tiempo')
        return None
    
    if(cuadroTexto9.get()==''):
        Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto13.get())-float(cuadroTexto12.get())))
        masa2=Q/abs(cp2*(float(cuadroTexto15.get())-float(cuadroTexto14.get())))
    else:
        masa2=float(cuadroTexto9.get())
    
    if(cuadroTexto8.get()==''):
        Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto15.get())-float(cuadroTexto14.get())))
        masa1=Q/abs(cp1*(float(cuadroTexto13.get())-float(cuadroTexto12.get())))
    else:
        masa1=float(cuadroTexto8.get())
    
    if(cuadroTexto12.get()==''):
        Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto15.get())-float(cuadroTexto14.get())))
        th1=float(cuadroTexto13.get())+(Q/(cp1*float(cuadroTexto8.get())))
    else:
        th1=float(cuadroTexto12.get())
    
    if(cuadroTexto13.get()==''):
        Q=abs(float(cuadroTexto9.get())*cp2*(float(cuadroTexto15.get())-float(cuadroTexto14.get())))
        th2=float(cuadroTexto12.get())-(Q/(cp1*float(cuadroTexto8.get())))
    else:
        th2=float(cuadroTexto13.get())
    
    if(cuadroTexto14.get()==''):
        Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto13.get())-float(cuadroTexto12.get())))
        tc1=float(cuadroTexto15.get())-(Q/(cp2*float(cuadroTexto9.get())))
    else:
        tc1=float(cuadroTexto14.get())
    
    if(cuadroTexto15.get()==''):
        Q=abs(float(cuadroTexto8.get())*cp1*(float(cuadroTexto13.get())-float(cuadroTexto12.get())))
        tc2=float(cuadroTexto14.get())+(Q/(cp2*float(cuadroTexto9.get())))
    else:
        tc2=float(cuadroTexto15.get())

    masa1tex.set(str(masa1))
    masa2tex.set(str(masa2))
    th1texto.set(str(th1))
    th2texto.set(str(th2))
    tc1texto.set(str(tc1))
    tc2texto.set(str(tc2))

    calorQ = masa2*cp2*(tc2-tc1)
    print(calorQ)
    variabletexto.set(str(calorQ))
    

    #Property data
    if(cuadroTexto10.get()==''):
        messagebox.showwarning('','el rd del fluido calliente no puede estar vacio')
        return None
    
    foiling1 = float(cuadroTexto10.get())
    if(cuadroTexto11.get()==''):
        messagebox.showwarning('','el rd del fluido frio no puede estar vacio')
        return None
    foiling2 = float(cuadroTexto11.get())
    if(cuadroTexto4.get()==''):
        messagebox.showwarning('','la viscosidad del fluido caliente no puede estar vacio')
        return None
    viscosidad1 = float(cuadroTexto4.get())
    if(cuadroTexto5.get()==''):
        messagebox.showwarning('','la viscosidad del fluido frio no puede estar vacio')
        return None
    viscosidad2 = float(cuadroTexto5.get())
    if(cuadroTexto6.get()==''):
        messagebox.showwarning('','la conductividad del fluido caliente no puede estar vacio')
        return None
    conductividad1 = float(cuadroTexto6.get())
    if(cuadroTexto7.get()==''):
        messagebox.showwarning('','la conductividad del fluido frio no puede estar vacio')
        return None
    conductividad2 = float(cuadroTexto7.get())
    if(cuadroTexto0.get()==''):
        messagebox.showwarning('','la densidad del fluido caliente no puede estar vacio')
        return None
    densidad1 = float(cuadroTexto0.get())
    if(cuadroTexto1.get()==''):
        messagebox.showwarning('','la densidad del fluido frio no puede estar vacio')
        return None
    densidad2 = float(cuadroTexto1.get())
    prandtl1 = cp1*viscosidad1/conductividad1
    print(prandtl1)
    prandtl1texto.set(str(prandtl1))
    prandtl2 = cp2*viscosidad2/conductividad2
    print(prandtl2)
    prandtl2texto.set(str(prandtl2))

    #Geometría plato
    if(cuadroTexto17.get()==''):
        messagebox.showwarning('','la conductividaqd del plato no puede estar vacio')
        return None
    conductividadplato = float(cuadroTexto17.get())
    if(cuadroTexto18.get()==''):
        messagebox.showwarning('','el lc del plato no puede estar vacio')
        return None
    lc = float(cuadroTexto18.get())
    if(cuadroTexto19.get()==''):
        messagebox.showwarning('','el ld del plato no puede estar vacio')
        return None
    lv = float(cuadroTexto19.get())
    if(cuadroTexto20.get()==''):
        messagebox.showwarning('','el lh del plato no puede estar vacio')
        return None
    lh = float(cuadroTexto20.get())
    if(cuadroTexto21.get()==''):
        messagebox.showwarning('','el dp del plato no puede estar vacio')
        return None
    diamport = float(cuadroTexto21.get())
    diamportm = diamport/1000
    print(diamportm)
    dptexto.set(str(diamportm))
    lp = lv - diamportm
    print(lp)
    lptextos.set(str(lp))
    lw = lh + diamportm
    print(lw)
    anchotexto.set(str(lw))
    areaproyectada = lp * lw
    if(cuadroTexto23.get()==''):
        messagebox.showwarning('','el espesor del plato no puede estar vacio')
        return None
    t_espesor = float(cuadroTexto23.get())
    t_espesorm = t_espesor/1000
    print(t_espesorm)
    espesortexto.set(str(t_espesorm))
    if(cuadroTexto25.get()==''):
        messagebox.showwarning('','el numero de placas del plato no puede estar vacio')
        return None
    numplacas = float(cuadroTexto25.get())
    numplacasutiles = numplacas - 2
    print(numplacasutiles)
    placasutexto.set(str(numplacasutiles))
    p_pitch = lc/numplacas
    print(p_pitch)
    pitchtexto.set(str(p_pitch))
    b_espaciado = p_pitch-t_espesorm
    print(b_espaciado)
    espaciadotexto.set(str(b_espaciado))
    ach = b_espaciado * lw
    if(cuadroTexto26.get()==''):
        messagebox.showwarning('','el area efectiva del plato no puede estar vacio')
        return None
    areaefectiva = float(cuadroTexto26.get())
    areaplaca = areaefectiva/numplacasutiles
    facampliacion = areaplaca/areaproyectada
    print(facampliacion)
    factortexto.set(str(facampliacion))
    dh = (2 * b_espaciado)/(facampliacion)
    print(dh)
    Dhtexto.set(str(dh))
    if(cuadroTexto27.get()==''):
        messagebox.showwarning('','el numero de pasos del plato no puede estar vacio')
        return None
    numpasos = float(cuadroTexto27.get())
    ncp = (numplacas-1)/(2*numpasos)
    viscosidadagua = 0.001
    
    mch1 = masa1/ncp
    mch2 = masa2/ncp
    gch1 = mch1/ach
    gch2 = mch2/ach
    reynolds1 = (gch1*dh)/viscosidad1
    print(reynolds1)
    reynolds1texto.set(str(reynolds1))
    reynolds2 = (gch2*dh)/viscosidad2
    print(reynolds2)
    reynolds2texto.set(str(reynolds2))
    
    #Calculo LMTD
    lmtd = 0
    if(math.log((th1-tc2)/(th2-tc1))<=0):
        lmtd= ((th1-tc2)+(th2-tc1))/2
    else:
        lmtd = ((th1-tc2)-(th2-tc1))/math.log((th1-tc2)/(th2-tc1))

    #Coeficientes de pelicula
    if(cuadroTexto24.get()==''):
        messagebox.showwarning('','el valor cheviron no puede estar vacio')
        return None
    cheviron = float(cuadroTexto24.get())
    ch1, n1, kp1, m1 = calcCheviron(cheviron, reynolds1)
    ch2, n2, kp2, m2 = calcCheviron(cheviron, reynolds2)
    nu1 = ch1 * (reynolds1 ** n1) * (prandtl1**(1/3))
    print(nu1)
    nussellhtexto.set(str(nu1))
    hhot = nu1 * conductividad1 / dh
    print(hhot)
    hcalientetexto.set(str(hhot))
    nu2 = ch2 * (reynolds2 ** n2) * (prandtl2**(1/3))
    print(nu2)
    nussellctexto.set(str(nu2))
    hcold = nu2 * conductividad2 / dh
    print(hcold)
    hfriotexto.set(str(hcold))

    #Coeficientes de transferencia de calor U
    tkw = t_espesorm / conductividadplato
    divihhot = 1 / hhot
    divihcold = 1 / hcold
    diviuc = tkw + divihhot + divihcold
    uc = diviuc ** (-1)
    print(uc)
    uctexto.set(str(uc))
    diviud = diviuc + foiling1 + foiling2
    ud = diviud ** (-1)
    print(ud)
    udtexto.set(str(ud))

    #CF
    cf = ud / uc
    print(cf)
    Cftexto.set(str(cf))
    qcleanw = uc * areaefectiva * lmtd
    qcleankw = qcleanw / 1000
    print(qcleankw)
    Qcleantexto.set(str(qcleankw))
    qdisenow = ud * areaefectiva * lmtd
    qdisenokw = qdisenow / 1000
    print(qdisenokw)
    Qdisenotexto.set(str(qdisenokw))

    #Factor de satisfacción
    cs = qdisenow/calorQ
    print(cs)
    Cstexto.set(str(cs))
    #Calculos de la caida de presión
    fhot = kp1/(reynolds1 ** m1)
    print(fhot)
    fhottexto.set(str(fhot))
    fcold = kp2/(reynolds2 ** m2)
    print(fcold)
    fcoldtexto.set(str(fcold))
    deltapchot = (4 * fhot) * (lv*numpasos/dh) * ((gch1**2)/(2*densidad1)) * ((viscosidad1/0.001) ** (-0.17))
    deltapchotpsi = deltapchot / 6895
    print(deltapchotpsi)
    Deltapchtexto.set(str(deltapchotpsi))
    deltapccold = (4 * fcold) * (lv*numpasos/dh) * ((gch2**2)/(2*densidad2)) * ((viscosidad2/0.001) ** (-0.17))
    deltapccoldpsi = deltapccold / 6895
    print(deltapccoldpsi)
    Deltapcctexto.set(str(deltapccoldpsi))
    gphot = masa1 / (math.pi * ((diamportm ** 2) / 4))
    gpcold = masa2 / (math.pi * ((diamportm ** 2) / 4))
    deltapphot = 1.4 * numpasos * ((gphot ** 2) / (2 * densidad1))
    deltapphotpsi = deltapphot / 6895
    print(deltapphotpsi)
    Deltapphtexto.set(str(deltapphotpsi))
    deltappcold = 1.4 * numpasos * ((gpcold ** 2) / (2 * densidad2))
    deltappcoldpsi = deltappcold / 6895
    print(deltappcoldpsi)
    Deltappctexto.set(str(deltappcoldpsi))
    deltapthot = deltapchotpsi + deltapphotpsi
    print(deltapthot)
    Deltapthtexto.set(str(deltapthot))
    deltaptcold = deltapccoldpsi + deltappcoldpsi
    print(deltaptcold)
    Deltaptctexto.set(str(deltaptcold))
    print('xd')

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()