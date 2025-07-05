from matplotlib import pyplot as plt

def przes_o_wektor(tab_pkt,wektor):
    x1=tab_pkt[0].x
    y1=tab_pkt[0].y
    x2=tab_pkt[1].x
    y2=tab_pkt[1].y
    plt.plot([x1, x2], [y1, y2], color='purple')
    #przesuniecie
    x1+=wektor[0]
    y1 += wektor[1]
    x2+=wektor[0]
    y2+=wektor[1]

    plt.plot([x1,x2],[y1,y2],color='red')
    plt.scatter([x1,x2],[y1,y2],color='orange')
    plt.grid(True)
    plt.title("Przesunieta")
    plt.legend(["prosta","przesunieta"])
    plt.show()


