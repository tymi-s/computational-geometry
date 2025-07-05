from matplotlib import pyplot as  plt
def odbicie(tab_pkt,punkt):
    x1 = tab_pkt[0].x
    y1 = tab_pkt[0].y
    y2 = tab_pkt[1].y
    x2 = tab_pkt[1].x
    x0=punkt[0]
    y0=punkt[1]

    #postać y = ax + b
    a=(y2-y1)/(x2-x1)
    b = y2-a*x2

    # zmiana do postaci Ax +Bx + C = 0
    A = a
    B=-1
    C =b

    # normalizacja:

    mianownik = A**2+B**2

    mx = x0 - 2 * A * (A * x0 + B * y0 + C) / mianownik
    my = y0 - 2 * B * (A * x0 + B * y0 + C) / mianownik

    #(mx,my) punkt odbity wzgledem prostej:
    plt.grid(True)
    plt.plot([x1,x2],[y1,y2], color='grey')
    plt.scatter([x1,x2],[y1,y2], color='black')
    plt.scatter(x0,y0, color='blue')
    plt.scatter(mx,my, color='skyblue')
    plt.title('Odbicie punktu w zgledem prostej')
    plt.legend(["prosta","punkty nalezace do prostej","poczatkowy","odbity"])
    plt.show()


