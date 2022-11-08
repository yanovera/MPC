import polytope.polytope as pc
import numpy as np
import matplotlib.pyplot as plt
import ppopt


def main():
    F = np.array([[1.0, 0.0],
                  [0.0, 1.0],
                  [-1.0, -0.0],
                  [-0.0, -1.0]])

    g = np.array([1.0, 1.0, 1.0, 1.0]).T

    p1 = pc.Polytope(F, g)

    v = np.array([[0.2, -0.2], [0.2, 0.4], [-0.3, 0.4], [-0.3, -0.5]])

    p2 = pc.qhull(v)

    vert = pc.extreme(p2)

    print(vert)

    p3 = pc.Polytope(F, np.array([1.5, 1.5, 0.0, 0.0]).T)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    s = pc.Region([p1, p2, p3])
    # s.plot()

    # p1.plot(ax)
    # p2.plot(ax)
    # p3.plot(ax)

    i = pc.intersect(p1, p3)

    # i.plot(ax)

    q1 = pc.qhull(np.array([[-1, 0], [0, 1], [0, -1]]))

    q2 = pc.qhull(np.array([[0, 1], [1, 0], [0, -1]]))

    u = pc.union(q1, q2)

    # u.plot(ax)

    a = s.list_poly

    p1_vertices = pc.extreme(a[0])

    h = pc.qhull(pc.extreme(a))
    h.plot(ax)

    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
