import numpy as np
import polytope.polytope as pc
import pytope as pt

def main():
    A = np.array([[1, 1],
                  [0, 1]])

    B = np.array([[0.5],
                  [1]])

    H = np.array([[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]])

    h = np.array([[25],
                 [5],
                 [25],
                 [5]])

    F = np.concatenate((H@A, H@A), axis=0)
    g = np.concatenate((h-H@B,h+H@B), axis=0)

    PreXe = pt.Polytope(F, g)

    PreXe.minimize_H_rep()

    Xe = pt.Polytope(H, h)

    intersection = PreXe and Xe

    print(intersection.A)
    print(intersection.b)



if __name__ == '__main__':
    main()
