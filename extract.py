import random as rnd
import numpy as np

def getRandomCurve(lenght,variance=50):
	randi = rnd.randint(1,variance)/variance
	a = list(range(lenght+1)) 
	b = list(a)
	for i in range(lenght+1):
		b[i] = (randi*i)
	return [a, b]

def getXAndY(text):
	text = text.replace(" ", "")
	idx = text.find("x")
	idy = text.find("y")
	x = int(text[0:idx])
	y = int(text[idx+1:idy])
	return x, y

def stripIneq(text):
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
		if idx > idr: x = -1 * int(x)
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
		if idy > idr: y = -1 * int(y)
		else: y = int(y)
	# Obtener la respuesta
	if idr > idx and idr > idy:
		r = int(text[idr+1:])
	# Obtener la orientacion # 0 Menor"<" | 1 Mayor">"
	#s = int(text.find(">")>0)
	# Obtener si hay igual o no # 0 No | 1 Si
	#e = max(0,int(text.find("=")>0))
	return x, y, r #,s,e

def generateCurve(x, y, r):
	xr = np.linspace(-50,50,50)
	yr = np.linspace(-50,50,50)
	if x == 0 and y != 0:
		yr = np.repeat(r, 50)
	if y == 0 and x != 0:
		xr = np.repeat(r, 50)
	else:
		yr = (r-x*xr)/y
	return xr, yr

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
		print("---------\n",i,": \n",stripIneq(i),sep="")
