import numpy
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("dane/Zadanie_2.csv", delimiter=";", header=None)
    print(data)
    eigenvalues, eigenvectors = numpy.linalg.eig(data)

    print("Eigenvalues:")
    print(eigenvalues)

    print("Eigenvectors:")
    print(eigenvectors)

    flipped = numpy.flip(data.values)
    print("Flipped:")
    print(flipped)

