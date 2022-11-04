import numpy
import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = pd.read_csv("dane/Zadanie_2.csv")
    print(data)
    # print(type(data))
    a, eig = numpy.linalg.eig(data)

    # flipped = numpy.flip(data)
    # print(flipped)

