import matplotlib.pyplot as plt


class Punkt:
    def __init__(self, id=0, x=0, y=0):
        self.id = id
        self.x = x
        self.y = y

class Elementy:
    def __init__(self,id =0,id_punktow=0):
        self.id = id
        self.id_punktow = id_punktow

punkty = []

# Odczytanie pliku NODES.txt
with open("NODES.txt", "r") as file:
    linie = file.readlines() # tworzenie tablichy z wspolrzednymi

print("Tablica z punktami: ",linie)

for l in linie:
    wartosci = l.split()  # Rozdzielenie spacjami. tablica wartosci staje sie tablica z wspolrzednymi kazdego puntku
    print(wartosci)
    if len(wartosci) == 3:
        id,x,y= map(int, wartosci)  #mapowanie wartości ze stringa na inta
        punkty.append(Punkt(id, x, y)) # ONA BEDZIE UZYWANA POZNIEJ TEZ
    else:
        print("NIEPOPRAWNY FORMAT PLIKU!!!")
        break



# Rysowanie punktów
for punkt in punkty:
    plt.scatter(punkt.x, punkt.y, label=f"ID {punkt.id}")

plt.grid(True)  # Włączenie siatki po ustawieniu punktów
plt.legend()  #legenda
plt.xlabel("OŚ X",fontsize=12)
plt.ylabel("OŚ Y",fontsize=12)
plt.show()

###################### RYSOWANIE KSZTAŁTÓW:

z_pliku = []

with open("ELEMENTS.txt", "r") as file:
    z_pliku = file.readlines()
    print("Tablica z elementami: ",z_pliku)

elementy = [] # to bedzie tablica obiektow typu Element
tmp =[]
for i in z_pliku:
    tmp=i.split() # tablica tmp przyjmuje postać jednej linijki z pliku ELEMENTS
    id_elementu = int(tmp[0])
    punktty = list(map(int,tmp[1:])) # tu sie tworzy tablica z id punktów polaczonych
    elementy.append(Elementy(id_elementu, punktty))# wywołanie konstruktora

print("Lista z obiektami klasy element: \n")
for i in elementy:
    print(i.id,i.id_punktow)

    if len(i.id_punktow) ==1:
        print(f"Element o id rownym {i.id} jest tylko punktem")
    if len(i.id_punktow) == 2:
        print(f"Element o id równym {i.id} jest odcinkiem")
    if len(i.id_punktow) == 3:
        print(f"Element o id równym {i.id} jest trójkątem")
    if len(i.id_punktow) >= 4:
        print(f"Element o id równym {i.id} jest wielokątem")





for element in elementy:

    point_ids = element.id_punktow # tablica z wszystkimi id punktów

    # tu bedą zbierane x i y kazdego punktu
    x_coords = []
    y_coords = []
    
    for point_id in point_ids:

        for punkt in punkty:#  punkt to tablica z punktami z pliku NODES
            if punkt.id == point_id:
                x_coords.append(punkt.x)
                y_coords.append(punkt.y)
                break


    if len(point_ids) >= 3:
        x_coords.append(x_coords[0])
        y_coords.append(y_coords[0])

    # Plot the element
    plt.fill(x_coords, y_coords,color='green', label=f"Element {element.id}")
    plt.plot(x_coords, y_coords, 'blue', label=f"Element {element.id}")


# zaznaczenie punktów dla wiekszej czytelnosci
for punkt in punkty:
    plt.scatter(punkt.x, punkt.y)
    plt.text(punkt.x, punkt.y, f"{punkt.id}", fontsize=9)

plt.grid(True)
plt.title("Elementy")
plt.legend()
plt.xlabel("OŚ X", fontsize=12)
plt.ylabel("OŚ Y", fontsize=12)
plt.show()


