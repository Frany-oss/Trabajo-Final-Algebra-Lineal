import extract as ext
import numpy as np
import matplotlib.pyplot as plt


figure = plt.figure(figsize=(5,4),dpi=100) 
subplot = figure.add_subplot(111)

inequations = ["y >= x","x <= 30", "y <= 20", "y <= 2x" ]
parameters = []
curves = []


for i in inequations:
	x, y, r, s = ext.stripIneq(i)
	parameters.append([x,y,r,s])
	xr, yr = ext.generateLine(x,y,r)
	curves.append([xr,yr])

intersections = ext.findIntersections(parameters)


#idx = np.argwhere(np.diff(np.sign(curves[0][1] - curves[1][1]))).flatten()
#plt.plot(curves[0][0][idx], curves[0][1][idx], 'ro')

# Graficar
for idx, i in enumerate(curves):
	subplot.plot(i[0],i[1],'--',label=inequations[idx])

# Graficar puntos
for i in intersections:
	plt.plot(i[0],i[1],color='black', marker='o',markersize=6)

# Rellenar el poligono formado por los puntos de interseccion
# plt.fill([x1,x2,x3,x1],[y1,y2,y3,y1],'red',alpha=0.5)


subplot.set_xlim(-5,70)
subplot.set_ylim(-5,70)

plt.legend()
plt.show()