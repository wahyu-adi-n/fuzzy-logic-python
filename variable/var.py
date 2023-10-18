class Variable:
    def kondisi(self, mins, median, maks, x):
        if x < mins or x > maks:
            return 0
        elif x >= mins and x <= median:
            return (x - mins) / (median - mins)
        elif x >= median and x <= maks:
            return (maks - x) / (maks - median)
