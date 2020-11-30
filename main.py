import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


import linear_programing as lp
import extract as ext

# ----------- GLOBALES ------------------------------------------------------------------------------

# Window (root)
window = tk.Tk()
window.title("Programacion Lineal")
window.config(bg="SystemButtonFace")

# Canvas
canvas = tk.Canvas(window, width=300, height=550)
canvas.grid() # .pack()

# Figure
figure = plt.figure(figsize=(5,4),dpi=100) 
subplot = figure.add_subplot(111)

# Gráfico
graph = FigureCanvasTkAgg(figure, master=window)
graph.get_tk_widget().grid(row=0, column=1)

# Mostrar toolbar
toolbar = tk.Frame(master=window)
toolbar.grid(row=1,column=1)
NavigationToolbar2Tk(graph, toolbar)

# Arreglos de las inecuaciones
inecuacionesLista, rectas, parametros = [], [], []
intersecciones, funcionObjetivo, poligono = [], [], []

# Textos Default
textoEjemploInecuacion = "Ejemplo: 2x-1.5y<=2"
textoEjemploFuncionObjetivo = "Ejemplo: 3x + 7y"

# ----------- FUNCIONES ------------------------------------------------------------------------------
def startLP():
	global funcionObjetivo
	entrada = textboxFunc.get()
	try:
		# Leer la funcion objetivo y guardar
		xi, yi, _, _, _ = ext.stripString(entrada)
		funcionObjetivo = [xi,yi]

		# Desactivar la escritura del Textbox funcion objetivo
		textboxFunc.configure(state="disabled")

		# Activa la escritura de Inecuaciones
		textboxAdd.config(state="normal")
		buttonAdd.config(state="normal")
	except:
		print("Funcion objetivo invalida")


def addInecuation():
	global graph, inecuacionesLista, intersecciones
	entrada = textboxAdd.get()

	try:
		# Agregar a la lista de string
		inecuacionesLista.append(entrada)

		# Agregar a la lista de parametros
		xi, yi, ri, si, ei = ext.stripString(entrada)
		parametros.append([xi,yi,ri,si,ei])

		# Agregar a la lista de lineas para graficas
		curvai = ext.generateLine(xi,yi,ri)
		rectas.append(curvai)

		# Encontrar las intersecciones
		intersecciones = ext.findIntersections(parametros)

		# Generar Grafico
		generarGrafico()

		# Quitar los espacios
		entrada = entrada.replace(" ", "")

		# Agregar al cuadro
		cuadroIneq.config(state="normal")
		cuadroIneq.insert("insert",entrada+"\n")
		cuadroIneq.config(state="disable")
		textboxAdd.delete(0,"end")
	except:
		print("Inecuacion invalida")


def generarGrafico():
	global graph, toolbar, rectas, intersecciones, poligono

	# Reiniciar la gráfica
	graph.get_tk_widget().grid_remove()
	toolbar.grid_remove()
	
	# Iniciar Figure
	figure = plt.figure(figsize=(5,4),dpi=100) 
	figure.add_axes([1,1,1,1])
	subplot = figure.add_subplot(111)

	# Graficar cada curva
	for i in range(len(inecuacionesLista)):
		subplot.plot(rectas[i][0], rectas[i][1], '--', label=inecuacionesLista[i])

	# Graficar cada interseccion
	for i in intersecciones:
		plt.plot(i[0],i[1],color='black', marker='o',markersize=6)

	# Graficar el poligono respuesta
	poligono = ext.getPolygon(parametros, intersecciones)
	plt.fill(poligono[0],poligono[1],'red',alpha=0.5)

	# Configuracion del subplot
	subplot.legend()
	subplot.grid()
	subplot.set_xlim(-5,100)
	subplot.set_ylim(-5,100)
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


def reset():
	global graph, toolbar, inecuacionesLista, rectas, parametros
		
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
	# Limpiar las listas
	inecuacionesLista.clear()   
	rectas.clear()
	parametros.clear()
	# Remover los graficos y la barra de herramientas
	graph.get_tk_widget().grid_remove()
	toolbar.grid_remove()   


# ----------- INTERFAZ ------------------------------------------------------------------------------

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