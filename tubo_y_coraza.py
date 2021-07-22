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
nombreLabel0=Label(miFrame, text='Masa Fluido frio(lb/h):')
nombreLabel0.grid(row=0,column=0,padx=10,pady=10)
cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=1,column=1,padx=10,pady=10)
nombreLabel1=Label(miFrame, text='Masa Fluido caliente(lb/h):')
nombreLabel1.grid(row=1,column=0,padx=10,pady=10)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=2,column=1,padx=10,pady=10)
nombreLabel2=Label(miFrame, text='cp caliente(btu/lb°F):')
nombreLabel2.grid(row=2,column=0,padx=10,pady=10)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=4,column=1,padx=10,pady=10)
nombreLabel3=Label(miFrame, text='temparatura 1 de fluido caliente(°F):')
nombreLabel3.grid(row=4,column=0,padx=10,pady=10)
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=5,column=1,padx=10,pady=10)
nombreLabel4=Label(miFrame, text='temperatura 2 de fluido caliente(°F):')
nombreLabel4.grid(row=5,column=0,padx=10,pady=10)
cuadroTexto5=Entry(miFrame)
cuadroTexto5.grid(row=6,column=1,padx=10,pady=10)
nombreLabel5=Label(miFrame, text='temperatura 1 fluido frio(°F):')
nombreLabel5.grid(row=6,column=0,padx=10,pady=10)
cuadroTexto6=Entry(miFrame)
cuadroTexto6.grid(row=7,column=1,padx=10,pady=10)
nombreLabel6=Label(miFrame, text='temperatura 2 fluido frio(°F):')
nombreLabel6.grid(row=7,column=0,padx=10,pady=10)
cuadroTexto7=Entry(miFrame)
cuadroTexto7.grid(row=3,column=1,padx=10,pady=10)
nombreLabel7=Label(miFrame, text='cp fluido frio(btu/lb°F):')
nombreLabel7.grid(row=3,column=0,padx=10,pady=10)
cuadroTexto8=ttk.Combobox(miFrame,values=[
                                    "1", 
                                    "1(1/4)",
                                    "2",
                                    "2(1/2)",
                                    "3",
                                    "4"],state="readonly")
cuadroTexto8.grid(row=8,column=1,padx=10,pady=10)
nombreLabel8=Label(miFrame, text='diametro tubo (cedula 40):')
nombreLabel8.grid(row=8,column=0,padx=10,pady=10)
cuadroTexto9=ttk.Combobox(miFrame,values=[
                                    "1", 
                                    "1(1/4)",
                                    "2",
                                    "2(1/2)",
                                    "3",
                                    "4"],state="readonly")
cuadroTexto9.grid(row=9,column=1,padx=10,pady=10)
nombreLabel9=Label(miFrame, text='diametro anulo(cedula 40):')
nombreLabel9.grid(row=9,column=0,padx=10,pady=10)
cuadroTexto10=Entry(miFrame)
cuadroTexto10.grid(row=10,column=1,padx=10,pady=10)
nombreLabel10=Label(miFrame, text='densidad fluido tubo(lb/ft^3):') 
nombreLabel10.grid(row=10,column=0,padx=10,pady=10)
cuadroTexto11=Entry(miFrame)
cuadroTexto11.grid(row=11,column=1,padx=10,pady=10)
nombreLabel11=Label(miFrame, text='viscosidad fluido tubo(cp):')
nombreLabel11.grid(row=11,column=0,padx=10,pady=10)
cuadroTexto12=Entry(miFrame)
cuadroTexto12.grid(row=12,column=1,padx=10,pady=10)
nombreLabel12=Label(miFrame, text='conductividad fluido tubo(btu/ft*h*°F):')
nombreLabel12.grid(row=12,column=0,padx=10,pady=10)
cuadroTexto13=Entry(miFrame)
cuadroTexto13.grid(row=13,column=1,padx=10,pady=10)
nombreLabel13=Label(miFrame, text='gravedad especifica anulo:')
nombreLabel13.grid(row=13,column=0,padx=10,pady=10)
cuadroTexto14=Entry(miFrame)
cuadroTexto14.grid(row=14,column=1,padx=10,pady=10)
nombreLabel14=Label(miFrame, text='viscosidad fluido anulo(cp):')
nombreLabel14.grid(row=14,column=0,padx=10,pady=10)
cuadroTexto15=Entry(miFrame)
cuadroTexto15.grid(row=15,column=1,padx=10,pady=10)
nombreLabel15=Label(miFrame, text='conductividad fluido anulo(btu/ft*h*°F):')
nombreLabel15.grid(row=15,column=0,padx=10,pady=10)
cuadroTexto16=Entry(miFrame)
cuadroTexto16.grid(row=16,column=1,padx=10,pady=10)
nombreLabel16=Label(miFrame, text='rd interna(h*ft^2*°F/btu):')
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
    densidad1 = 59.76
    densidad2 = 59.87
    cp1 = 0.92
    cp2 = 1
    viscocidad1 = 0.75
    viscocidad2 = 0.77
    viscocidadft1 = viscocidad1 * 2.42
    viscocidadft2 = viscocidad2 * 2.42
    conductividad1 = 0.3
    conductividad2 = 0.36
    masa1 = 50000
    rd1 = 0.004 / 2
    rd2 = 0.004 / 2
    TH1 = 144
    TH2 = 113
    tc1 = 77
    tc2 = 100
    temprom1 = (TH1 + TH2) / 2
    temprom2 = (tc1 + tc2) / 2
    Q = masa1 * cp1 * (TH1 - TH2)
    print(Q)
    masa2 = Q/(cp1*(tc2-tc1))
    udiseño = 150
    lmtd = ((TH1-tc2)-(TH2-tc1))/math.log((TH1-tc2)/(TH2-tc1))
    R = (tc1-tc2)/(TH2-TH1)
    S = (TH2-TH1)/(tc1-TH1)
    F = ((math.sqrt((R**2)+1))*math.log((1-S)/(1-R*S)))/((R-1)*math.log((2-S*(R+1-math.sqrt((R**2)+1)))/(2-S*(R+1+math.sqrt((R**2)+1)))))
    area = Q/(lmtd*F*150)
    print(area)
    lmtd = lmtd * F
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
    numeroTubos = math.ceil(areaflujo/areatubointft)
    print(numeroTubos)
    areatransferenciain = math.pi*(diamintin*L)
    areatransferenciaft = areatransferenciain/12
    numPasos = math.ceil(area/(areatransferenciaft*numeroTubos))
    if(numPasos % 2 != 0):
        numPasos += 1
    print(numPasos)
    tubosTotales = numeroTubos * numPasos
    print(tubosTotales)
    return None

botonCalcular=Button(raiz,text='enviar',command=codigoBoton)
botonCalcular.pack()

raiz.mainloop()