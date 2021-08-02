import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

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
nombreLabel2=Label(miFrame, text='cp del fluido frio(btu/lb°F):')
nombreLabel2.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=4,column=1,padx=10,pady=10)
nombreLabel3=Label(miFrame, text='cp del fluido caliente(btu/lb°F):')
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
cuadroTexto8=Entry(miFrame)
cuadroTexto8.grid(row=8,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='masa del fluido caliente(lb/h):')
nombreLabel8.grid(row=8,column=0,padx=10,pady=10)
cuadroTexto9=Entry(miFrame)
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
cuadroTexto12=Entry(miFrame)
cuadroTexto12.grid(row=12,column=1,padx=10,pady=10)
nombreLabel12=Label(miFrame, text='temperatura 1 fluido caliente(°F):')
nombreLabel12.grid(row=12,column=0,padx=10,pady=10)
cuadroTexto13=Entry(miFrame)
cuadroTexto13.grid(row=13,column=1,padx=10,pady=10)
nombreLabel13=Label(miFrame, text='temperatura 2 fluido caliente(°F):')
nombreLabel13.grid(row=13,column=0,padx=10,pady=10)
cuadroTexto14=Entry(miFrame)
cuadroTexto14.grid(row=14,column=1,padx=10,pady=10)
nombreLabel14=Label(miFrame, text='temperatura 1 fluido frio(°F):')
nombreLabel14.grid(row=14,column=0,padx=10,pady=10)
cuadroTexto15=Entry(miFrame)
cuadroTexto15.grid(row=15,column=1,padx=10,pady=10)
nombreLabel15=Label(miFrame, text='temperatura 2 fluido frio(°F):')
nombreLabel15.grid(row=15,column=0,padx=10,pady=10)
cuadroTexto17=Entry(miFrame)
cuadroTexto17.grid(row=17,column=1,padx=10,pady=10)
nombreLabel17=Label(miFrame, text='conductividad plato:')
nombreLabel17.grid(row=17,column=0,padx=10,pady=10)
cuadroTexto18=Entry(miFrame)
cuadroTexto18.grid(row=18,column=1,padx=10,pady=10)
nombreLabel18=Label(miFrame, text='Lc plato(m):')
nombreLabel18.grid(row=18,column=0,padx=10,pady=10)
cuadroTexto19=Entry(miFrame)
cuadroTexto19.grid(row=19,column=1,padx=10,pady=10)
nombreLabel19=Label(miFrame, text='Lv plato(m):')
nombreLabel19.grid(row=19,column=0,padx=10,pady=10)
cuadroTexto20=Entry(miFrame)
cuadroTexto20.grid(row=0,column=3,padx=10,pady=10)
nombreLabel20=Label(miFrame, text='Lh plato (m):')
nombreLabel20.grid(row=0,column=2,padx=10,pady=10)
cuadroTexto21=Entry(miFrame)
cuadroTexto21.grid(row=1,column=3,padx=10,pady=10)
nombreLabel21=Label(miFrame, text='Dp plato(mm):')
nombreLabel21.grid(row=1,column=2,padx=10,pady=10)
cuadroTexto22=Entry(miFrame)
cuadroTexto22.grid(row=2,column=3,padx=10,pady=10)
nombreLabel22=Label(miFrame, text='valor de  PITCH:')
nombreLabel22.grid(row=2,column=2,padx=10,pady=10)
cuadroTexto23=Entry(miFrame)
cuadroTexto23.grid(row=3,column=3,padx=10,pady=10)
nombreLabel23=Label(miFrame, text='espesor plato(mm):')
nombreLabel23.grid(row=3,column=2,padx=10,pady=10)
cuadroTexto24=ttk.Combobox(miFrame,values=[
                                    "30", 
                                    "45",
                                    "60"
                                    ],state="readonly")
cuadroTexto24.grid(row=4,column=3,padx=10,pady=10)
nombreLabel24=Label(miFrame, text='cheviron:')
nombreLabel24.grid(row=4,column=2,padx=10,pady=10)
cuadroTexto25=Entry(miFrame)
cuadroTexto25.grid(row=5,column=3,padx=10,pady=10)
nombreLabel25=Label(miFrame, text='numero placas plato:')
nombreLabel25.grid(row=5,column=2,padx=10,pady=10)
cuadroTexto26=Entry(miFrame)
cuadroTexto26.grid(row=6,column=3,padx=10,pady=10)
nombreLabel26=Label(miFrame, text='Area efectiva (m^2):')
nombreLabel26.grid(row=6,column=2,padx=10,pady=10)
cuadroTexto27=Entry(miFrame)
cuadroTexto27.grid(row=7,column=3,padx=10,pady=10)
nombreLabel27=Label(miFrame, text='K Conductividad del tubo (btu/ft*h*°F):')
nombreLabel27.grid(row=7,column=2,padx=10,pady=10)
cuadroTexto28=Entry(miFrame)
cuadroTexto28.grid(row=8,column=3,padx=10,pady=10)
nombreLabel28=Label(miFrame, text='rd int referido externo:')
nombreLabel28.grid(row=8,column=2,padx=10,pady=10)
cuadroTexto29=Entry(miFrame)
cuadroTexto29.grid(row=9,column=3,padx=10,pady=10)
nombreLabel29=Label(miFrame, text='Rd ext*(Di/De) referido externo:')
nombreLabel29.grid(row=9,column=2,padx=10,pady=10)
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
nombreLabelo18=Label(miFrame, text="numero de baffles=2*Longitud de los tubos en metros:")
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

nombreLabelo38=Label(miFrame, text="resistencia conductiva interna interno:")
nombreLabelo38.grid(row=14,column=4,padx=10,pady=10)
nombreLabelo39=Label(miFrame, textvariable=Resistcondinterna_interna)
nombreLabelo39.grid(row=14,column=5,padx=10,pady=10)
nombreLabelo40=Label(miFrame, text="resistencia convectiva interna interno:")
nombreLabelo40.grid(row=15,column=4,padx=10,pady=10)
nombreLabelo41=Label(miFrame, textvariable=Resistconvinterna_interna)
nombreLabelo41.grid(row=15,column=5,padx=10,pady=10)
nombreLabelo42=Label(miFrame, text="resistencia convectiva externa interno:")
nombreLabelo42.grid(row=16,column=4,padx=10,pady=10)
nombreLabelo43=Label(miFrame, textvariable=Resistconvexterna_interna)
nombreLabelo43.grid(row=16,column=5,padx=10,pady=10)
nombreLabelo44=Label(miFrame, text="resistencia conductiva interna externo:")
nombreLabelo44.grid(row=17,column=4,padx=10,pady=10)
nombreLabelo45=Label(miFrame, textvariable=Resistcondinterna_externa)
nombreLabelo45.grid(row=17,column=5,padx=10,pady=10)
nombreLabelo46=Label(miFrame, text="resistencia convectiva interna externo:")
nombreLabelo46.grid(row=18,column=4,padx=10,pady=10)
nombreLabelo47=Label(miFrame, textvariable=Resistconvinterna_externa)
nombreLabelo47.grid(row=18,column=5,padx=10,pady=10)
nombreLabelo48=Label(miFrame, text="resistencia convectiva externa externo:")
nombreLabelo48.grid(row=19,column=4,padx=10,pady=10)
nombreLabelo49=Label(miFrame, textvariable=Resistconvexterna_externa)
nombreLabelo49.grid(row=19,column=5,padx=10,pady=10)

#---------------funcion que llama el boton para calcular todo-----------#
def codigoBoton():

    #Tabla fluidos
    masa2 = 140
    cp1 = 4183
    cp2 = 4178
    th1 = 65
    th2 = 45
    tc1 = 22
    tc2 = 42
    calorQ = masa2*cp2*(tc2-tc1)
    print(calorQ)
    masa1 = calorQ/(cp1*(th1-th2))

    #Property data
    foiling1 = 0.00005
    foiling2 = 0.000001
    viscosidad1 = 0.000509
    viscosidad2 = 0.000766
    conductividad1 = 0.645
    conductividad2 = 0.617
    densidad1 = 985
    densidad2 = 995
    prandtl1 = cp1*viscosidad1/conductividad1
    print(prandtl1)
    prandtl2 = cp2*viscosidad2/conductividad2
    print(prandtl2)

    #Geometría plato
    conductividadplato = 17.5
    lc = 0.38
    lv = 1.55
    lh = 0.43
    diamport = 200
    diamportm = diamport/1000
    print(diamportm)
    lp = lv - diamportm
    print(lp)
    lw = lh + diamportm
    print(lw)
    areaproyectada = lp * lw
    t_espesor = 0.6
    t_espesorm = t_espesor/1000
    print(t_espesorm)
    numplacas = 105
    numplacasutiles = numplacas - 2
    print(numplacasutiles)
    p_pitch = lc/numplacas
    print(p_pitch)
    b_espaciado = p_pitch-t_espesorm
    print(b_espaciado)
    ach = b_espaciado * lw
    areaefectiva = 110
    areaplaca = areaefectiva/numplacasutiles
    facampliacion = areaplaca/areaproyectada
    print(facampliacion)
    dh = (2 * b_espaciado)/(facampliacion)
    print(dh)
    numpasos = 1
    ncp = (numplacas-1)/(2*numpasos)
    viscosidadagua = 0.001
    
    mch1 = masa1/ncp
    mch2 = masa2/ncp
    gch1 = mch1/ach
    gch2 = mch2/ach
    reynolds1 = (gch1*dh)/viscosidad1
    print(reynolds1)
    reynolds2 = (gch2*dh)/viscosidad2
    print(reynolds2)
    
    #Calculo LMTD
    lmtd = 0
    if(math.log((th1-tc2)/(th2-tc1))<=0):
        lmtd= ((th1-tc2)+(th2-tc1))/2
    else:
        lmtd = ((th1-tc2)-(th2-tc1))/math.log((th1-tc2)/(th2-tc1))

    #Coeficientes de pelicula
    nu1 = 0.3 * (reynolds1 ** 0.663) * (prandtl1**(1/3))
    print(nu1)
    hhot = nu1 * conductividad1 / dh
    print(hhot)
    nu2 = 0.3 * (reynolds2 ** 0.663) * (prandtl2**(1/3))
    print(nu2)
    hcold = nu2 * conductividad2 / dh
    print(hcold)

    #Coeficientes de transferencia de calor U
    tkw = t_espesorm / conductividadplato
    divihhot = 1 / hhot
    divihcold = 1 / hcold
    diviuc = tkw + divihhot + divihcold
    uc = diviuc ** (-1)
    print(uc)
    diviud = diviuc + foiling1 + foiling2
    ud = diviud ** (-1)
    print(ud)

    #CF
    cf = ud / uc
    print(cf)
    qcleanw = uc * areaefectiva * lmtd
    qcleankw = qcleanw / 1000
    print(qcleankw)
    qdisenow = ud * areaefectiva * lmtd
    qdisenokw = qdisenow / 1000
    print(qdisenokw)

    #Factor de satisfacción
    cs = qdisenow/calorQ
    print(cs)

    #Calculos de la caida de presión
    fhot = 1.441/(reynolds1 ** 0.206)
    print(fhot)
    fcold = 1.441/(reynolds2 ** 0.206)
    print(fcold)
    deltapchot = (4 * fhot) * (lv*numpasos/dh) * ((gch1**2)/(2*densidad1)) * ((viscosidad1/0.001) ** (-0.17))
    deltapchotpsi = deltapchot / 6895
    print(deltapchotpsi)
    deltapccold = (4 * fcold) * (lv*numpasos/dh) * ((gch2**2)/(2*densidad2)) * ((viscosidad2/0.001) ** (-0.17))
    deltapccoldpsi = deltapccold / 6895
    print(deltapccoldpsi)
    gphot = masa1 / (math.pi * ((diamportm ** 2) / 4))
    gpcold = masa2 / (math.pi * ((diamportm ** 2) / 4))
    deltapphot = 1.4 * numpasos * ((gphot ** 2) / (2 * densidad1))
    deltapphotpsi = deltapphot / 6895
    print(deltapphotpsi)
    deltappcold = 1.4 * numpasos * ((gpcold ** 2) / (2 * densidad2))
    deltappcoldpsi = deltappcold / 6895
    print(deltappcoldpsi)
    deltapthot = deltapchotpsi + deltapphotpsi
    print(deltapthot)
    deltaptcold = deltapccoldpsi + deltappcoldpsi
    print(deltaptcold)


botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()