import extract as ext
import numpy as np
import matplotlib.pyplot as plt


figure = plt.figure(figsize=(5,4),dpi=100) 
subplot = figure.add_subplot(111)

#inequations = ["y >= x","x <= 30", "y <= 20", "y <= 2x" ]
#inequations = ["0.33x + 0.16y <= 80", "0.33x + 0.5y <= 100" ]
inequations = ["x <= 40", "y <= 10"]
parameters = []
curves = []

for i in inequations:
	x, y, r, s, e = ext.stripString(i)
	parameters.append([x,y,r,s,e])
	xr, yr = ext.generateLine(x,y,r,-1000,1000)
	curves.append([xr,yr])

intersections = ext.findIntersections(parameters)

# Obtener coordenadas aprobadas
polygon = ext.getPolygon(parameters, intersections)


def getLine(polygon):
	visited = [0] * len(polygon[0])
	pass


plt.fill(polygon[0],polygon[1],'red',alpha=0.5)

getLine(polygon)


# Graficar
for idx, i in enumerate(curves):
	subplot.plot(i[0],i[1],'--',label=inequations[idx])

# Graficar puntos
for i in intersections:
	plt.plot(i[0],i[1],color='black', marker='o',markersize=6)


xAxis, yAxis = ext.getMargins(intersections)
subplot.set_xlim(-5,xAxis)
subplot.set_ylim(-5,yAxis)
subplot.spines['left'].set_position('zero')
subplot.spines['right'].set_color('none')
subplot.spines['bottom'].set_position('zero')
subplot.spines['top'].set_color('none')


plt.legend()
plt.show()