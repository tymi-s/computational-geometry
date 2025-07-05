def StartingPoint(tab):

    p0 = tab[0]
    print(f"before: {p0.x},{p0.y}")
    for p in tab[1:]:
      if(p0.y >p.y):
          p0=p

    # w przypadku gdy są dwa punkty o tych samych, najmniejszych współrzędnych y:
    for m in tab:
        if(p0.y == m.y and p0.x != m.x):
            if(p0.x > m.x):
                p0 =m
    print(f"after: ({p0.x},{p0.y})")

    return p0