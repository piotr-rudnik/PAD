import numpy as np

import seaborn
seaborn.set()

if __name__ == '__main__':
    A = np.array([0, 3, 2, 5])
    B = np.array([0, 3, 1, 4])

    added_vectors = A + B
    subtracted_vectors = A - B
    a_times_4 = A * 4
    len_b = B.size
    dot_product = np.dot(A, B)

    print("A: " + str(A))
    print("B: " + str(B))

    print("Added vectors: " + str(added_vectors))
    print("Subtracted vectors: " + str(subtracted_vectors))
    print("A times 4: " + str(a_times_4))
    print("Dot: " + str(dot_product))
    print("Len of B: " + str(len_b))
