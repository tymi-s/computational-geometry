from punkty_class import punkty
def odczyt():

    new = open("punkty.txt", "r")



    tab_punktow = []

    tab_punkt = new.readlines()
    print(tab_punkt)

    for i in tab_punkt:
        tab_punkt = i.split()
        print(tab_punkt)
        id_p = tab_punkt[0]
        x = int(tab_punkt[1])
        y = int(tab_punkt[2])
        tab_punktow.append(punkty(id_p, x, y))

    # printing the list with all the points read from a file:

    for i in tab_punktow:
        print(f"punkt numer {i.id} i jego koordynaty: ({i.x},{i.y})")  # i am so fucking smart god demn

    return tab_punktow