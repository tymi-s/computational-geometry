from matplotlib import pyplot as plt
from genereateRandomPoints import *
from triangulation import *


rang = int(input("Enter the range of points: "))
points = []
pointsX = genereateRandomPoints(rang,"X")
pointsY = genereateRandomPoints(rang,"Y")

xmin = min(pointsX)
xmax = max(pointsX)
ymin = min(pointsY)
ymax = max(pointsY)

# margines który ustala jak duży względem puntktów ma być prostokąt
margin_x = (xmax - xmin) * 0.40
margin_y = (ymax - ymin) * 0.40

# prostokat z marginesem
rectangleX = [xmin - margin_x, xmax + margin_x, xmax + margin_x, xmin - margin_x]
rectangleY = [ymin - margin_y, ymin - margin_y, ymax + margin_y, ymax + margin_y]

#SUPERTRÓJKĄT
supertriangleX = [rectangleX[0] - margin_x, rectangleX[1] + margin_x, (rectangleX[0] + rectangleX[1])/2]
supertriangleY = [rectangleY[0] - margin_y, rectangleY[0] - margin_y, rectangleY[2] + 2*margin_y]

# zamknięcie trójkata
#supertriangleX.append(supertriangleX[0])
#supertriangleY.append(supertriangleY[0])

triangulation(supertriangleX,supertriangleY,pointsX,pointsY)


plt.fill(supertriangleX, supertriangleY,color='blue')# POLE TROJKATA
plt.scatter(supertriangleX[:-1], supertriangleY[:-1], color='red')#PUNKTY TRÓJKATA
#plt.scatter(rectangleX, rectangleY,color='purple')#PUNKTY PROSTOKĄTA
#plt.fill(rectangleX, rectangleY,color='lightblue')# POLE PROSTOKĄTA
plt.scatter(pointsX, pointsY,color = "orange")# PUNKTY DO TRIANGULACJI


plt.grid(True)
plt.legend(["Pole supertrójkąta","Punkty supertrójkąta","Punkty do triangulacji","Punkty prostokąta","pole prostokąta"])
plt.show()
