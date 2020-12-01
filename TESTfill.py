import extract as ext
import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(5,4),dpi=125) 
subplot = figure.add_subplot(111)

A = [7, 6, 0, 3, 0]
B = [0.5, 6, 6, 7.5, 7.5]

for i, j in zip(A, B):
	subplot.plot(i,j,color='black', marker='o',markersize=6)

plt.fill(A,B,'red',alpha=0.5)


polygon = [(7,0.5),(3.7,7.5),(0,6),(3,7.5),(0,7.5)]

def getDistance(a,b):
	x1,y1 = a
	x2,y2 = b
	return ((x2-x1)**2 + (y2-y1)**2)**0.5


def joinLines(polygon):
	pass
	

print(getDistance((2,2),(3,4)))

plt.show()