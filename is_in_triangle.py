from dist2 import *
from matplotlib import pyplot as plt
from Heron import *
def is_in_triangle(TriangleField,ChechPoint,tab_x,tab_y):

    #FIRST TRIANGLE:
    tab_x0 =[]
    tab_x0.append(ChechPoint[0])
    tab_x0.append(tab_x[0])
    tab_x0.append(tab_x[1])
    tab_x0.append(ChechPoint[0])
    print("\n\n",tab_x0)

    tab_y0 = []
    tab_y0.append(ChechPoint[1])
    tab_y0.append(tab_y[0])
    tab_y0.append(tab_y[1])
    tab_y0.append(ChechPoint[1])
    print(tab_y0)

    abc0 =dist2(tab_x0,tab_y0)
    print(f"abc0 = {abc0}")

    S1=Heron(abc0)
    print(f"S1 = {S1}")
    #SECOND TRIANGLE:

    tab_x1 = []
    tab_x1.append(ChechPoint[0])
    tab_x1.append(tab_x[1])
    tab_x1.append(tab_x[2])
    tab_x1.append(ChechPoint[0])
    print("\n",tab_x1)

    tab_y1 = []
    tab_y1.append(ChechPoint[1])
    tab_y1.append(tab_y[1])
    tab_y1.append(tab_y[2])
    tab_y1.append(ChechPoint[1])
    print(tab_y1)

    abc1 =dist2(tab_x1,tab_y1)
    print(f"abc1 = {abc1}")
    S2 = Heron(abc1)
    print(f"S2 = {S2}")

    #THIRD TRIANGLE:

    tab_x2 = []
    tab_x2.append(ChechPoint[0])
    tab_x2.append(tab_x[2])
    tab_x2.append(tab_x[3])
    tab_x2.append(ChechPoint[0])
    print("\n",tab_x2)

    tab_y2 = []
    tab_y2.append(ChechPoint[1])
    tab_y2.append(tab_y[2])
    tab_y2.append(tab_y[3])
    tab_y2.append(ChechPoint[1])
    print(tab_y2)
    abc2 =dist2(tab_x2,tab_y2)
    print(f"abc2 = {abc2}")
    S3 = Heron(abc2)
    print(f"S3 = {S3}")
    r = S1+S2+S3
    r = round(r,3)
    TriangleField = round(TriangleField,3)
    print(f"S1 + S2 + S3 = {r}")
    if (r == TriangleField):
        print("\n\nPOINT IS INSIDE THE TRIANGLE !!!")
        print(f"{r} == {TriangleField}")
    else:
        print("POINT IS NOT INSIDE THE TRIANGLE!!!")
        print(f"{r} != {TriangleField}")

