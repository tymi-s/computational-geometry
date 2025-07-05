
def gdzie_punkt(tab_pkt,punkt):
    x1=tab_pkt[0].x
    y1=tab_pkt[0].y
    x2=tab_pkt[1].x
    y2=tab_pkt[1].y

    # punkt ktory jest sprawdzany:
    x0=punkt[0]
    y0=punkt[1]
    iloczyn_wektorowy = ((x2 -x1) * (y0 - y1)) -((y2-y1) * (x0 - x1))

    if iloczyn_wektorowy > 0:
        print(f"\npunkt ({x0},{y0}) lezy po lewej stronie prostej!")
    elif iloczyn_wektorowy < 0:
        print(f"\npunkt ({x0},{y0}) lezy po prawej stronie prostej!")
    elif iloczyn_wektorowy == 0:
        print(f"\npunkt ({x0},{y0}) nalezy do prostej!")