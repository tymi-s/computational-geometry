from math import *
from matplotlib import pyplot as plt
from is_in_circle import *


def triangulacja(r, tabx, taby, front):
    new_front = front.copy()
    to_plot_x = []
    to_plot_y = []

    # wewnętrzne punkty

    internal_points = []

    # PRZETWARZANIE KRAWEDZI
    def process_edge(i, j):

        a = sqrt((front[j][0] - front[i][0]) ** 2 + (front[j][1] - front[i][1]) ** 2)
        print(f"a: {a}", end=" ")

        # bo dzielenie przez 0 bylo
        if a < 0.0001:
            print(f"Pomijam krawędź {i} -> {j} o długości blisko zero")
            return False


        h = (a * sqrt(3)) / 2
        h = round(h, 4)
        print(f"h: {h}", end="\n")

        # srodek krawedzi
        mid_x = (front[j][0] + front[i][0]) / 2
        mid_y = (front[j][1] + front[i][1]) / 2

        # Wektor wzdłuż krawędzi
        edge_x = front[j][0] - front[i][0]
        edge_y = front[j][1] - front[i][1]

        # WSPOLRZEDNE WEKTORA PROSTOPADLEGO DO KRAWEDZI
        normal_x = -edge_y
        normal_y = edge_x

        # NORMALIZACJA WEKTORA NORMALNEGO:
        normal_length = sqrt(normal_x ** 2 + normal_y ** 2)

        # bo dzieliło przez 0:
        if normal_length < 0.0001:
            print(f"Pomijam krawędź {i} -> {j} - wektor normalny ma długość blisko zero")
            return False

        normal_x /= normal_length
        normal_y /= normal_length

        # centrum figury
        centroid_x = sum(p[0] for p in front) / len(front)
        centroid_y = sum(p[1] for p in front) / len(front)

        to_centroid_x = centroid_x - mid_x
        to_centroid_y = centroid_y - mid_y

        # Iloczyn skalarny wektorow zeby sprawdzic czy wektor normalny skierowany jest do srodka okręgu
        dot_product = normal_x * to_centroid_x + normal_y * to_centroid_y

        if dot_product < 0:
            normal_x = -normal_x
            normal_y = -normal_y


        x0 = mid_x + normal_x * h
        y0 = mid_y + normal_y * h

        # Sprawdzenie promienia
        in_circle, closest_idx = is_in_circle(r, x0, y0, internal_points)

        if in_circle:

            x0, y0 = internal_points[closest_idx]
            print(f"Punkt ({x0}, {y0}) już istnieje - używam go ponownie")
        else:

            internal_points.append([x0, y0])


        to_plot_x.append(front[i][0])
        to_plot_x.append(x0)
        to_plot_y.append(front[i][1])
        to_plot_y.append(y0)

        new_front[i] = [x0, y0]
        return True


    for i in range(len(front) - 1):
        process_edge(i, i + 1)
        plt.figure(figsize=(10, 8))
        plt.plot(to_plot_x, to_plot_y, color='black')
        plt.scatter(to_plot_x, to_plot_y, color='red')
        plt.plot(tabx, taby, color='blue')
        plt.grid(True)
        plt.axis('equal')
        plt.show()
    # ostatnia krawedz
    process_edge(len(front) - 1, 0)


    to_plot_x.append(to_plot_x[0])
    to_plot_y.append(to_plot_y[0])







    return new_front