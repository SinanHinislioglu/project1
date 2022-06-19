"""

Creating a graphical interface program that allows drawing the necessary graphics to calculate the optimum asphalt ratio

"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd #importiert alles mit Umbenennen des Namensbereiches
import numpy as np
from tkinter import * # importiert alle Funktionen (Methoden) aus dem Modul Tkinter
from sympy import *
from functools import partial

root=Tk() #initialisiert Tkinter, um Tk-Root-Widget zu erstellen.
root.title("Marshall Mix Design Graphs")
Marshall_Data = pd.read_csv("MarshallDesign.csv", delimiter=";") # liest eine Datei mit durch Kommas getrennten Werten (csv) in DataFrame.

print(Marshall_Data)
x_asphalt = Marshall_Data["Asphalt"] # erstelt eine Variable für die Asphaltdaten in der Datendatei
print(type(x_asphalt))
new_x_asphalt = np.arange(3, 7, 0.01) # generiert Daten zwischen min und max. asphalt daten
x=symbols("x") # x deklariert als Funktionsvariable
y=symbols("y")

def Stability(): # erstellt eine Funktion für das Stabilitätsdiagramm

    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.Stability, "bo") # gezeichnet die Asphaltverhältnis - Dichte diagramm
    plt.title("Asphalt Content vs. Stability")
    plt.ylabel("Stability (kg)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_stability = Marshall_Data["Stability"]
    c_stability = np.polyfit(x_asphalt, y_stability, 2) # erstellt ein Polynom 2. Grades für die Stabilitätsdaten
    a= float("%.2f"% c_stability[0]) # umgewandelt die Polynomkoeffizient in zweilige Zahlen
    b= float("%.2f"% c_stability[1])
    c= float("%.2f"% c_stability[2])
    print(c_stability)
    f_stability1 = np.poly1d(c_stability)
    f_stability=a*x**2+b*x+c
    print("Stability equation : ",f_stability)
    f2 = diff(f_stability) # 1. Ableitung des Polynom
    eq = Eq(f2, 0)
    AC_stability = solve((eq), x) #berechnet der x Wert, der die Stabilität maximiert
    d1=float("%.2f" % AC_stability[0])
    print("Asphalt ratio corresponding to maximum stability (%) : " ,d1)
    y_stability_model = f_stability1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_stability_model, 'red') #erstellt die Stabilitätskurve mit den erzeugten new Asphalt daten
    plt.show(block=False)
Stability_button = Button(root, text="Stability", command=Stability) #aufruft die Funktion
Stability_button.pack(fill=X, expand=1) #erstellt Button für die Stabilität


def Density(): # erstellt eine Funktion für das Densitysdiagramm

    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.Density, "bo") #gezeichnet die Asphaltverhältnis - Dichte diagramm
    plt.title("Asphalt Content vs. Density")
    plt.ylabel("Density (gr/cm3)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_density = Marshall_Data["Density"]
    c_density = np.polyfit(x_asphalt, y_density, 2) # erstellt ein Polynom 2. Grades für die Densitysdaten
    a = float("%.2f" % c_density[0]) #umgewandelt die Polynomkoeffizient in zweilige Zahlen
    b = float("%.2f" % c_density[1])
    c = float("%.2f" % c_density[2])
    f_density1 = np.poly1d(c_density)
    f_density=a*x**2+b*x+c
    print("Density equation : ", f_density)
    f2 = diff(f_density) #1. Ableitung des Polynom
    eq = Eq(f2, 0)
    AC_density = solve((eq), x) #berechnet der x Wert, der die Density maximiert
    d2=float("%.2f" % AC_density[0])
    print("Asphalt ratio corresponding to maximum density (%):", d2)
    y_density_model = f_density1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_density_model, 'red') #erstellt die Densityskurve mit den erzeugten new Asphalt daten
    plt.show(block=False)
Density_button = Button(root, text="Density", command=Density) #aufruft die Funktion
Density_button.pack(fill=X, expand=1) #erstellt Button für die Density

def Flow():  # erstellt eine Funktion für das Flowsdiagramm

    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.Flow, "bo") #gezeichnet die Asphaltverhältnis - Flow diagramm
    plt.title("Asphalt Content vs. Flow")
    plt.ylabel("Flow (mm)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_flow = Marshall_Data["Flow"]
    c_flow = np.polyfit(x_asphalt, y_flow, 1) # erstellt ein linear equation für die Flowssdaten
    a = float("%.2f" % c_flow[0])#umgewandelt die equationseffizient in zweilige Zahlen
    b = float("%.2f" % c_flow[1])
    f_flow1 = np.poly1d(c_flow)
    f_flow=a*x+b
    print("Flow equation : ", f_flow)
    eq = Eq(f_flow, 3) #berechnet der x Wert, der die Flow 3 machts
    AC_flow= solve((eq), x)
    d3=float("%.2f" % AC_flow[0])
    y_flow_model = f_flow1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_flow_model, 'red') #erstellt die Flowskurve mit den erzeugten new Asphalt daten
    plt.show(block=False)
Flow_button = Button(root, text="Flow", command=Flow) #aufruft die Funktion
Flow_button.pack(fill=X, expand=1) #erstellt Button für die Flow

def VMA(): # erstellt eine Funktion für das Flowsdiagramm


    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.VMA, "bo") #gezeichnet die Asphaltverhältnis -VMA diagramm
    plt.title("Asphalt Content vs.VMA")
    plt.ylabel("Voids in Mineral Aggregate (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_VMA = Marshall_Data["VMA"]
    c_VMA = np.polyfit(x_asphalt, y_VMA, 2) # erstellt ein Polynom 2. Grades für die VMAs daten
    a = float("%.2f" % c_VMA[0]) #umgewandelt die equationseffizient in zweilige Zahlen
    b = float("%.2f" % c_VMA[1])
    c = float("%.2f" % c_VMA[2])
    f_VMA1 = np.poly1d(c_VMA)
    f_VMA=a*x**2+b*x+c
    eq = Eq(f_VMA, y) #berechnet der x Wert, der die VMA 13 machts
    y_VMA_model = f_VMA1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_VMA_model, 'red') #erstellt die VMAskurve mit den erzeugten new Asphalt daten
    print("VMA equation : ",f_VMA)
    plt.show(block=False)

VMA_button = Button(root, text="VMA", command=VMA) #aufruft die Funktion
VMA_button.pack(fill=X, expand=1) #erstellt Button für VMA

def VFA(): # erstellt eine Funktion für das Flowsdiagramm

    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.VFA, "bo")
    plt.title("Asphalt Content vs. VFA")
    plt.ylabel("Voids Filled with Asphalt (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_VFA=Marshall_Data["VFA"]
    c_VFA = np.polyfit(x_asphalt, y_VFA, 1) # erstellt ein linear equation für die Flowssdaten
    a = float("%.2f" % c_VFA[0]) #umgewandelt die equationseffizient in zweilige Zahlen
    b = float("%.2f" % c_VFA[1])
    f_VFA1 = np.poly1d(c_VFA)
    f_VFA=a*x+b
    print("VFA Equation : ",f_VFA)
    eq = Eq(f_VFA, 70) #berechnet der x Wert, der die VFA 70 machts
    AC_VFA = solve((eq), x)
    y_VFA_model = f_VFA1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_VFA_model, 'red') #erstellt die VFAskurve mit den erzeugten new Asphalt daten
    plt.show(block=False)

VFA_button=Button(root,text="VFA",command=VFA) #aufruft die Funktion
VFA_button.pack(fill=X, expand=1) #erstellt Button für VFA

def Void(): # erstellt eine Funktion für das Flowsdiagramm


    plt.close()
    plt.plot(Marshall_Data.Asphalt, Marshall_Data.Void, "bo")
    plt.title("Asphalt Content vs. Void Ratio")
    plt.ylabel("Void Ratio (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_void = Marshall_Data["Void"]
    c_void = np.polyfit(x_asphalt, y_void, 1) # erstellt ein linear equation für die Flowssdaten
    a = float("%.2f" % c_void[0]) #umgewandelt die equationseffizient in zweilige Zahlen
    b = float("%.2f" % c_void[1])
    f_void1 = np.poly1d(c_void)
    f_void = a*x+b
    print("Void Equation : ",f_void)
    eq = Eq(f_void, 4) #berechnet der x Wert, der die Void 4 machts
    AC_Void = solve((eq), x)
    y_void_model = f_void1(new_x_asphalt)
    plt.plot(new_x_asphalt, y_void_model, 'red') #erstellt die Voidskurve mit den erzeugten new Asphalt daten
    plt.show(block=False)


Void_button=Button(root,text="Void",command=Void) #aufruft die Funktion
Void_button.pack(fill=X, expand=1)

Stability()
Density()
Flow()
VMA()
VFA()
Void()

def AllMarshallGraphs(): #erstellt eine Funktion um alle Grafiken zusammen zu zeichnen
    x_asphalt = Marshall_Data["Asphalt"]
    y_stability = Marshall_Data["Stability"]
    y_density = Marshall_Data["Density"]
    y_flow = Marshall_Data["Flow"]
    y_VMA = Marshall_Data["VMA"]
    y_VFA = Marshall_Data["VFA"]
    y_void = Marshall_Data["Void"]

    plt.close()
    plt.subplot(2, 3, 1)
    plt.plot(x_asphalt, y_stability, "bo")
    plt.title("Asphalt Content vs. Stability")
    plt.ylabel("Stability (kg)")
    plt.grid()
    y_stability = Marshall_Data["Stability"]
    c_stability = np.polyfit(x_asphalt, y_stability, 2)
    f_stability = np.poly1d(c_stability)
    y_stability_model = f_stability(new_x_asphalt)
    plt.plot(new_x_asphalt, y_stability_model, 'red')

    plt.subplot(2, 3, 2)
    plt.plot(x_asphalt, y_density, "bo")
    plt.title("Asphalt Content vs. Density")
    plt.ylabel("Density (gr/cm3)")
    plt.grid()
    y_density = Marshall_Data["Density"]
    c_density = np.polyfit(x_asphalt, y_density, 2)
    f_density = np.poly1d(c_density)
    y_density_model = f_density(new_x_asphalt)
    plt.plot(new_x_asphalt, y_density_model, 'red')

    plt.subplot(2, 3, 3)
    plt.plot(x_asphalt, y_flow, "bo")
    plt.title("Asphalt Content vs. Flow")
    plt.ylabel("Flow (mm)")
    plt.grid()
    y_flow = Marshall_Data["Flow"]
    c_flow = np.polyfit(x_asphalt, y_flow, 1)
    f_flow = np.poly1d(c_flow)
    y_flow_model = f_flow(new_x_asphalt)
    plt.plot(new_x_asphalt, y_flow_model, 'red')

    plt.subplot(2, 3, 4)
    plt.plot(x_asphalt, y_VMA, "bo")
    plt.title("Asphalt Content vs.VMA")
    plt.ylabel("Voids in Mineral Aggregate (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_VMA = Marshall_Data["VMA"]
    c_VMA = np.polyfit(x_asphalt, y_VMA, 2)
    f_VMA = np.poly1d(c_VMA)
    y_VMA_model = f_VMA(new_x_asphalt)
    plt.plot(new_x_asphalt, y_VMA_model, 'red')

    plt.subplot(2, 3, 5)
    plt.plot(x_asphalt, y_VFA, "bo")
    plt.title("Asphalt Content vs. VFA")
    plt.ylabel("Voids Filled with Asphalt (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_VFA = Marshall_Data["VFA"]
    c_VFA = np.polyfit(x_asphalt, y_VFA, 2)
    f_VFA = np.poly1d(c_VFA)
    y_VFA_model = f_VFA(new_x_asphalt)
    plt.plot(new_x_asphalt, y_VFA_model, 'red')

    plt.subplot(2, 3, 6)
    plt.plot(x_asphalt, y_void, "bo")
    plt.title("Asphalt Content vs. Void Ratio")
    plt.ylabel("Void Ratio (%)")
    plt.grid()
    plt.xlabel("Asphalt Content (%)")
    y_void = Marshall_Data["Void"]
    c_void = np.polyfit(x_asphalt, y_void, 2)
    f_void = np.poly1d(c_void)
    y_void_model = f_void(new_x_asphalt)
    plt.plot(new_x_asphalt, y_void_model, 'red')
    plt.show(block=False)


button = Button(root, text="All_Graphs", command=AllMarshallGraphs) #aufruft die Funktion
button.pack(fill=X, expand=1)

but= Button(root, text='Quit', command=root.quit) #aufruft die root.quit Funktion
but.pack(fill=BOTH, expand=1)


root.mainloop() #ausführt der Tkinter-Ereignisschleife.
