import numpy
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn

seaborn.set()
import numpy.ma as ma

if __name__ == '__main__':
    data = pd.read_csv("dane/Seattle2014.csv")['PRCP'].values

    inches = data / 254.0

    no_rain_days = inches[inches == 0]
    rain_days = inches[inches != 0]
    over_0_5_inch = inches[inches > 0.5]
    under_0_2_inch = rain_days[rain_days < 0.2]

    print(f"Number of days without rain   : {len(no_rain_days)}")
    print(f"Number of days with rain      : {len(rain_days)}")
    print(f"Days with more than 0.5 inches: {len(over_0_5_inch)}")
    print(f"Rainy days with < 0.2 inches  : {len(under_0_2_inch)}")

    mask_rainy_days = data == 0
    masked_rainy_data = ma.masked_array(data, mask=mask_rainy_days)

    median_2014 = np.ma.median(masked_rainy_data)

    summer_mask = [not (172 < i < 262) for i in range(0, len(inches))]
    non_summer_mask = [(172 < i < 262) for i in range(0, len(inches))]

    sunny_data = ma.masked_array(inches, mask=summer_mask)
    non_sunny_data = ma.masked_array(masked_rainy_data, mask=non_summer_mask)

    print("Median precip on rainy days in 2014 (inches):" + str(median_2014))
    print("Median precip on summer days in 2014 (inches):" + str(np.ma.median(sunny_data)))
    print("Max precip on summer days in 2014 (inches):" + str(np.ma.max(sunny_data)))
    print("Median precip on non-summer rainy days in 2014 (inches):" + str(np.ma.median(non_sunny_data)))
