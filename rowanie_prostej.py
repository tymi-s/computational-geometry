import numpy as np
from matplotlib import pyplot as plt
def rownanie_prostej(tab_pkt):
    x1 = tab_pkt[0].x
    y1 = tab_pkt[0].y
    x2 = tab_pkt[1].x
    y2 = tab_pkt[1].y

    a = (y2-y1)/(x2-x1)
    b=y1 -a*x1
    print(f"\nrównanie prostej to: {a}x + {b}")

    x_v= [x1,x2]
    y_v= [y1,y2]

    plt.scatter(x_v, y_v, color='skyblue')
    plt.plot(x_v, y_v,color='navy')
    plt.grid(True)
    plt.title('rownanie prostej')
    plt.legend(["punkty", "prosta"])
    plt.show()

    parametry_prostej = [a,b]
    return parametry_prostej

