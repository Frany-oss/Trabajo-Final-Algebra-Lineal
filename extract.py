import random as rnd
import numpy as np

def stripString(text):
	# Revisar si el string esta vacio
	x = text[0]

	# Quitar los espacios
	text = text.replace(" ", "")

	# Obtener la posicion del <, > o =
	idr = max(text.find("<"), text.find(">"), text.find("="))
	x, y, r = 0, 0, 0

	# Obtener x si esta presente
	if (idx:=text.find("x")) >= 0:
		start = max(text[:idx].rfind("y"),
					text[:idx].rfind("<"),
					text[:idx].rfind(">"),
					text[:idx].rfind("="))
		x = text[start+1:idx]
		if x == "" or x == "+": x = 1
		if x == "-": x = -1
		if idx > idr and idr != -1: x = -1 * int(x)
		else: x = int(x)

	# Obtener y si esta presente
	if (idy:=text.find("y")) >= 0:
		start = max(text[:idy].rfind("x"),
					text[:idy].rfind("<"),
					text[:idy].rfind(">"),
					text[:idy].rfind("="))
		y = text[start+1:idy]
		if y == "" or y == "+": y = 1
		if y == "-": y = -1
		if idy > idr and idr != -1: y = -1 * int(y)
		else: y = int(y)

	# Obtener la respuesta
	if idr > idx and idr > idy:
		r = int(text[idr+1:])

	# Obtener la orientacion # 0 Menor"<" | 1 Mayor">"
	s = int(text.find(">")>0)

	# Obtener si hay igual o no # 0 No | 1 Si
	#e = max(0,int(text.find("=")>0))

	return x, y, r ,s #,e

def generateLine(x, y, r, minVal=-300, maxVal=300):
	xr = np.linspace(minVal, maxVal, 20)
	yr = np.linspace(minVal, maxVal, 20)
	if x == 0 and y != 0:
		# En el caso de que se tenga que graficar una linea horizontal
		yr = np.repeat(r, 20)
	elif y == 0 and x != 0:
		# En el caso de que se tenga que graficar una linea vertical
		xr = np.repeat(r, 20)
	else:
		# Graficar la recta normalmente
		yr = (r-x*xr)/y
	return xr, yr

def findIntersections(parameters):
	intersections = set()
	for i in parameters:
		for j in parameters:
			if i != j:
				x1, y1, r1, _ = i
				x2, y2, r2, _ = j
				try:
					# Se igualan las ecuaciones para hallar las intersecciones
					xr = (r1*y2 - r2*y1)/(x1*y2 - x2*y1)
					yr = (r1*x2 - r2*x1)/(y1*x2 - y2*x1)
					intersections.add((xr,yr))
				except:
					pass
	return list(intersections)

if __name__ == "__main__":
	ejemplos = ["2x + 3y <= 9",
		"-2x - 4y > 4",
		"x + y < 1",
		"x > -9",
		"y <= 0",
		"x > y",
		"y <= x",
		"y > 3x",
		"-3y <= -2x",
		"-7x > -10y",
		"-y > -x",
		"-x > -y",
		"-x <= 3",
		"y - x < 4"
	]

	for i in ejemplos:
		print("---------\n",i,": \n",stripString(i),sep="")
