import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

import linear_programing as lp
import extract as ext

# ----------- GLOBALES ------------------------------------------------------------------------------
#graph, toolbar
primeraVez = True
listaInecuaciones = []

# ----------- FUNCIONES ------------------------------------------------------------------------------
def startLP():
    # Desactivar la escritura del Textbox funcion objetivo
    textboxFunc.configure(state="disabled")

    # Ejecutar funcion
    pass


def generarGrafico(xAxis, yAxis):
    global graph, toolbar

    # Graph
    figure = Figure(figsize=(4,3),dpi=100) 
    subplot = figure.add_subplot(111) 
    subplot.plot(xAxis,yAxis) # primera curva 
    subplot.plot(yAxis,xAxis) # segunda curva 
    graph = FigureCanvasTkAgg(figure, master=window)
    graph.get_tk_widget().grid(row=0, column=1)
    
    # Toolbar
    toolbar = tk.Frame(master=window)
    toolbar.grid(row=1,column=1)
    NavigationToolbar2Tk(graph, toolbar)



def addInecuation():
    global graph, toolbar, primeraVez, listaInecuaciones

    entrada = textboxAdd.get()+"\n"
    if entrada != "\n":
        # Agregar a la lista
        listaInecuaciones.append(entrada)
        
        # Agregar al cuadro
        cuadroIneq.config(state="normal")
        cuadroIneq.insert("insert",entrada)
        cuadroIneq.config(state="disable")
        textboxAdd.delete(0,"end")

        # Resetear Grafico
        if not primeraVez:
            graph.get_tk_widget().grid_remove()
            toolbar.grid_remove()

        # Generar Grafico
        primeraVez = False
        xAxis = list(range(100,0,-10))
        yAxis = list(range(10))
        generarGrafico(xAxis,yAxis)

        # MAS MAS MAS
    pass

def reset():
    global graph, toolbar, primeraVez, listaInecuaciones
    
    # Limpiar textbox de funcion objetivo
    textboxFunc.configure(state="normal")
    textboxFunc.delete(0,"end")
    textboxFunc.insert(0, "Ejemplo: ax + by")

    # Limpiar textbox de inecuaciones
    textboxAdd.delete(0,"end")
    textboxAdd.insert(0,"Ejemplo: 2x+3y<=4")

    # Limpiar cuadro list de inecuaciones
    cuadroIneq.configure(state="normal")
    cuadroIneq.delete("1.0",tk.END)
    cuadroIneq.configure(state="disable")

    # Limpiar la lista de inecuaciones
    listaInecuaciones.clear()

    # Remover los graficos y la barra de herramientas
    if not primeraVez:
            graph.get_tk_widget().grid_remove()
            toolbar.grid_remove()

    # Reiniciar la primera vez
    primeraVez = True


# ----------- PROGRAMA ------------------------------------------------------------------------------
# window
window = tk.Tk()
window.title("Programacion Lineal")
window.config(bg="SystemButtonFace")

#Canvas
canvas = tk.Canvas(window, width=250, height=500)
canvas.grid() # .pack()

# Etiqueta Funcion Objetivo
labelFunc = tk.Label(window, text="Ingrese funcion objetivo:")
labelFunc.config(font=("Consolas",13))
canvas.create_window(125, 10, window=labelFunc)

# Textbox Funcion Objetivo
textboxFunc = ttk.Entry(window, justify=tk.CENTER, font=("Consolas",13))
textboxFunc.insert(0, "Ejemplo: ax + by")
canvas.create_window(125, 35, window=textboxFunc)

# Boton Estabecer Funcion Objetivo
buttonSet = tk.Button(window, text="Establecer",command=startLP, bg='palegreen', font=("Consolas",13)) 
canvas.create_window(125, 70, window=buttonSet)

# Etiqueta Inecuaciones
labelAdd = tk.Label(window, text="Ingrese inecuaciones:")
labelAdd.config(font=("Consolas",13))
canvas.create_window(125, 105, window=labelAdd)

# Textbox Añadir Inecuacion
textboxAdd = ttk.Entry(window, justify=tk.CENTER, font=("Consolas",13))
textboxAdd.insert(0, "Ejemplo: 2x+3y<=4")
canvas.create_window(125, 130, window=textboxAdd)

# Boton Añadir Inecuacion
buttonAdd = tk.Button(window, text="Añadir",command=addInecuation, bg='palegreen', font=("Consolas",13)) 
canvas.create_window(125, 165, window=buttonAdd)

# Text Widget Lista de Inecuaciones
cuadroIneq = tk.Text(window, width=19, height=11, padx=5, pady=5,bg='SystemButtonFace', font=("Consolas",13),state="disable")
canvas.create_window(125, 320, window=cuadroIneq)

# Boton Reiniciar
buttonAdd = tk.Button(window, text="Reiniciar",command=reset, bg='pink', font=("Consolas",13)) 
canvas.create_window(125, 475, window=buttonAdd)

# Loop Principal
window.mainloop()
