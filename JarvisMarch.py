from IloczynWektorowy import *
from ClassPoint import *
def JARVIS(punkty,p0):
    
    IWW= 0
    iddd=0
    T = [p0]
    current = p0
    
    while True:
        nex= None
        for i in punkty:
            if(i!=current):
                nex = i
                break

        #if nex is None:  # Jeśli nie ma innych punktów
        #    return T

        for i in punkty:
            if i != current and i != nex:
                # Obliczenie orientacji (current -> nex -> i)
                orientation = IW(current, nex, i)
                if orientation > 0:  # Punkt i jest bardziej na lewo niż nex
                    nex = i

        if nex == p0:
            break

        T.append(nex)
        current = nex

    T.append(p0)
    print("\nLISTA T:")
    for i in T:
        print(f"{i.idd},({i.x},{i.y})")


                
    
    return T