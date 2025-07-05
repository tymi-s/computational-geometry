def mediana(wartosci):





    if len(wartosci) % 2 == 0:
        x = wartosci[len(wartosci) // 2]
        y = wartosci[len(wartosci) // 2-1]
        mediana = (x+y)/2

    else:
        x=(len(wartosci) -1) /2
        mediana=wartosci[int(x)]

    print(f"Mediana to: {mediana}")

    return mediana




