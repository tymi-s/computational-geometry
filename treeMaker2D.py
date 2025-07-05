from drzewo2D import*
def treeMaker2D(korzen, wymiar="x"):
    if len(korzen.punkty) == 1:
        korzen.wartosc = korzen.punkty[0]
        return
    else:
        # Sortujemy punkty według odpowiedniego wymiaru
        if wymiar == "x":
            korzen.punkty.sort(key=lambda punkt: punkt[0])  #Sortowanie po x
        else:
            korzen.punkty.sort(key=lambda punkt: punkt[1])  # Sortowanie po y

        print(f"\n\nPRZEJSCIE NA PUNKTY ({wymiar}): {korzen.punkty}")


        if len(korzen.punkty) % 2 == 0:
            indeks_mediany = len(korzen.punkty) // 2 - 1
        else:
            indeks_mediany = len(korzen.punkty) // 2

        # Przygotuj listy dla lewego i prawego poddrzewa
        lewa = korzen.punkty[:indeks_mediany + 1]
        prawa = korzen.punkty[indeks_mediany + 1:]

        # Pobierz wartość mediany (punkt podziału)
        if wymiar == "x":
            m = korzen.punkty[indeks_mediany][0]  # wartosc x mediany
        else:
            m = korzen.punkty[indeks_mediany][1]  # wartość y mediany


        korzen.wartosc = m

        print(f"NOWA WARTOSC OJCA ({wymiar}): {korzen.wartosc}")
        print(f"LEWA:  {lewa}")
        print(f"PRAWA: {prawa}")


        korzen.left = drzewo2D(lewa, wymiar)
        korzen.right = drzewo2D(prawa, wymiar)


        if wymiar == "x":
            korzen.y_tree = drzewo2D(korzen.punkty, "y")
            treeMaker2D(korzen.y_tree, "y")


        treeMaker2D(korzen.left, wymiar)
        treeMaker2D(korzen.right, wymiar)


# inicjowanie budowania drzewa
def createRangeTree2D(punkty):
    root = drzewo2D(punkty)
    treeMaker2D(root)
    return root