import polytope.polytope as pc
import numpy as np
import matplotlib.pyplot as plt
from pytope import Polytope as pt
from ppopt.geometry import polytope as pp


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

    p2_vertices = pc.extreme(a[1])

    p3_vertices = pc.extreme(a[2])

    all_vertices = np.concatenate((p1_vertices, p2_vertices, p3_vertices))

    h = pc.qhull(all_vertices)

    # h.plot(ax)

    p1_pt = pt(pc.extreme(p1))

    p2_pt = pt(pc.extreme(p2))

    madd = p1_pt + p2_pt

    pdiff = p1_pt - p2_pt

    p1_pt.plot(ax, facecolor='red')

    pdiff.plot(ax, facecolor='green')

    p2_pt.plot(ax, facecolor='blue')

    plt.xlim([-1.5, 2])
    plt.ylim([-1.5, 2])

    plt.show()

    p1_pp = pp.Polytope(p1.A, p1.b)
    p1_pp = pp.Polytope(p1_pt.A, p1_pt.b)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
