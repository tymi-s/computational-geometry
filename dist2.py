from math import *


#def dist2(p1,p2):
#    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

# will return a lenght of every side of triangle:


def dist2(tab_x,tab_y):

    res = []
    for i in range(len(tab_x)-1):
        dis =(((tab_x[i] - tab_x[i+1])**2) +((tab_y[i] - tab_y[i+1])**2))**0.5
        res.append(dis)



    return res