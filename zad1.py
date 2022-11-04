import numpy
import pandas as pd
import numpy as np

# done
if __name__ == '__main__':
    data = pd.read_csv("dane/president_heights.csv")
    heights = np.array(data['height(cm)'])

    avg = numpy.average(heights)
    std = numpy.std(heights)
    min = numpy.min(heights)
    max= numpy.max(heights)

    median = numpy.median(heights)
    p25 = numpy.percentile(heights, 25)
    p75 = numpy.percentile(heights, 75)

    print("Mean height:" + str(avg))
    print("Standard deviation:" + str(std))
    print("Minimum height:" + str(min))
    print("Maximum height:" + str(max))
    print("Median: " + str(median))
    print("25th percentile: " + str(p25))
    print("27th percentile: " + str(p75))

