from mediana import mediana
from drzewo import drzewo


def treeMaker(korzen):
    if len(korzen.wartosc) == 1:
        return
    else:
        print(f"\n\nPRZEJSCIE NA TABLICE: {korzen.wartosc}")


        # obliczenie indeksu mediany
        if len(korzen.wartosc) % 2 == 0:
            indeks_mediany = len(korzen.wartosc) // 2 - 1
        else:
            indeks_mediany = len(korzen.wartosc) // 2

        # przypisanie mediany
        m = korzen.wartosc[indeks_mediany]


        lewa = []
        prawa = []


        for i in range(indeks_mediany + 1):
            lewa.append(korzen.wartosc[i])

        for i in range(indeks_mediany + 1, len(korzen.wartosc)):
            prawa.append(korzen.wartosc[i])


        korzen.wartosc = m

        print(f"NOWA WARTOSC OJCA: {korzen.wartosc}")
        print(f"LEWA:  {lewa}")
        print(f"PRAWA: {prawa}")


        korzen.left = drzewo(lewa)
        korzen.right = drzewo(prawa)


        treeMaker(korzen.left)
        treeMaker(korzen.right)