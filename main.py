import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

import linear_programing as lp
import extract as ext

# ----------- GLOBALES ------------------------------------------------------------------------------
# global graph, toolbar # Definidos en generarGrafico
primeraVez = True
inecuacionesLista = []
curvas = []

# Textos Default
textoEjemploInecuacion = "Ejemplo: 2x-3y<=2"
textoEjemploFuncionObjetivo = "Ejemplo: ax + by"


# ----------- FUNCIONES ------------------------------------------------------------------------------
def startLP():
	entrada = textboxFunc.get()
	if entrada != "" and entrada != textoEjemploFuncionObjetivo:
		# Desactivar la escritura del Textbox funcion objetivo
		textboxFunc.configure(state="disabled")

		# Activa la escritura de Inecuaciones
		textboxAdd.config(state="normal")
		buttonAdd.config(state="normal")

		# Ejecutar funcion


def generarGrafico():
	global graph, toolbar, primeraVez, curvas

	# Reiniciar la gráfica
	if not primeraVez:
		graph.get_tk_widget().grid_remove()
		toolbar.grid_remove()
	primeraVez = False
	
	# Iniciar Figure
	figure = Figure(figsize=(5,4),dpi=100) 
	subplot = figure.add_subplot(111)

	# Graficar cada curva
	for i in range(len(inecuacionesLista)):
		subplot.plot(curvas[i][0], curvas[i][1], '--', label=inecuacionesLista[i])

	# Configuracion del subplot
	subplot.legend()
	subplot.grid()
	subplot.set_xlim(-5,50)
	subplot.set_ylim(-5,50)
	subplot.spines['left'].set_position('zero')
	subplot.spines['right'].set_color('none')
	subplot.spines['bottom'].set_position('zero')
	subplot.spines['top'].set_color('none')

	# Gráfico
	graph = FigureCanvasTkAgg(figure, master=window)
	graph.get_tk_widget().grid(row=0, column=1)
	
	# Mostrar toolbar
	toolbar = tk.Frame(master=window)
	toolbar.grid(row=1,column=1)
	NavigationToolbar2Tk(graph, toolbar)


def addInecuation():
	global graph, toolbar, primeraVez, inecuacionesLista

	entrada = textboxAdd.get()
	if entrada != "" and entrada != textoEjemploInecuacion:
		# Quitar los espacios
		entrada = entrada.replace(" ", "")

		# Agregar al cuadro
		cuadroIneq.config(state="normal")
		cuadroIneq.insert("insert",entrada+"\n")
		cuadroIneq.config(state="disable")
		textboxAdd.delete(0,"end")

		# Agregar a la lista
		inecuacionesLista.append(entrada)

		# Agregar a la lista de curvas
		xi, yi, ri = ext.stripIneq(entrada)
		curvai = ext.generateCurve(xi,yi,ri)
		curvas.append(curvai)

		# Generar Grafico
		generarGrafico()
		# MAS MAS MAS


def reset():
	global graph, toolbar, primeraVez, inecuacionesLista
		
	# Limpiar textbox de funcion objetivo
	textboxFunc.configure(state="normal")
	textboxFunc.delete(0,"end")
	textboxFunc.insert(0, textoEjemploFuncionObjetivo)   
	# Limpiar textbox de inecuaciones
	textboxAdd.delete(0,"end")
	textboxAdd.insert(0,textoEjemploInecuacion)
	textboxAdd.config(state="disable")  
	# Limpiar cuadro list de inecuaciones
	cuadroIneq.configure(state="normal")
	cuadroIneq.delete("1.0",tk.END)
	cuadroIneq.configure(state="disable")   
	# Desactivar el boton de Añadir
	buttonAdd.config(state="disable")   
	# Limpiar la lista de inecuaciones
	inecuacionesLista.clear()   
	# Remover los graficos y la barra de herramientas
	if not primeraVez:
		graph.get_tk_widget().grid_remove()
		toolbar.grid_remove()   
	# Reiniciar la primera vez
	primeraVez = True


# ----------- INTERFAZ ------------------------------------------------------------------------------
# window
window = tk.Tk()
window.title("Programacion Lineal")
window.config(bg="SystemButtonFace")

#Canvas
canvas = tk.Canvas(window, width=300, height=550)
canvas.grid() # .pack()

# Etiqueta Funcion Objetivo
labelFunc = tk.Label(window, text="Ingrese funcion objetivo:")
labelFunc.config(font=("Consolas",15))
canvas.create_window(150, 10, window=labelFunc)

# Textbox Funcion Objetivo
textboxFunc = ttk.Entry(window, justify="center", font=("Consolas",15))
textboxFunc.insert(0, textoEjemploFuncionObjetivo)
canvas.create_window(150, 40, window=textboxFunc)

# Boton Estabecer Funcion Objetivo
buttonSet = tk.Button(window, text="Establecer",command=startLP, bg='palegreen', font=("Consolas",15)) 
canvas.create_window(150, 80, window=buttonSet)

# Etiqueta Inecuaciones
labelAdd = tk.Label(window, text="Ingrese inecuaciones:")
labelAdd.config(font=("Consolas",15))
canvas.create_window(150, 125, window=labelAdd)

# Textbox Añadir Inecuacion
textboxAdd = ttk.Entry(window, justify="center", font=("Consolas",15))
textboxAdd.insert(0, textoEjemploInecuacion)
textboxAdd.config(state="disabled")
canvas.create_window(150, 155, window=textboxAdd)

# Boton Añadir Inecuacion
buttonAdd = tk.Button(window, text="Añadir",command=addInecuation, bg='palegreen', font=("Consolas",15))
buttonAdd.config(state="disable")
canvas.create_window(150, 195, window=buttonAdd)

# Text Widget Lista de Inecuaciones
cuadroIneq = tk.Text(window, width=19, height=11, padx=5, pady=5,bg='SystemButtonFace', font=("Consolas",15),state="disable")
canvas.create_window(150, 360, window=cuadroIneq)

# Boton Reiniciar
buttonReset = tk.Button(window, text="Reiniciar",command=reset, bg='pink', font=("Consolas",15)) 
canvas.create_window(150, 525, window=buttonReset)

# Loop Principal
window.mainloop()
