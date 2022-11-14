import numpy as np

from pytope import Polytope

import matplotlib.pyplot as plt


def main():
    F = np.array([[1.0, 0.0],
                  [0.0, 1.0],
                  [-1.0, -0.0],
                  [-0.0, -1.0]])

    g = np.array([1.0, 1.0, 1.0, 1.0]).T

    p1 = Polytope(F, g)

    v = np.array([[0.2, -0.2], [0.2, 0.4], [-0.3, 0.4], [-0.3, -0.5]])

    p2 = Polytope(v)

    vert = p2.V

    print(vert)

    p3 = Polytope(F, np.array([1.5, 1.5, 0.0, 0.0]).T)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    s = [p1, p2, p3]

    colors = ['red', 'blue', 'green']

    for i, p in enumerate(s):
        p.plot(ax, facecolor=colors[i])

    plt.xlim([-1.5, 2])
    plt.ylim([-1.5, 2])



    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()