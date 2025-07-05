from matplotlib import pyplot as plt
from matplotlib.patches import Circle


def n_kat(n, a, b, R):

    fig, ax = plt.subplots()
    circle = Circle((a, b), R, color='purple', fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.set_xlim(a - R - 1, a + R + 1)
    ax.set_ylim(b - R - 1, b + R + 1)
    plt.grid(True)

    
    plt.show()