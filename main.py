import numpy as np
import pandas as pd

if __name__ == '__main__':
    print("--------------")
    arr = np.random.random(10)
    print(arr)
    print("--------------")
    print(arr[arr < 0.5])
