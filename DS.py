import matplotlib.pyplot as plt

import pandas as pd

data = [12, 15, 14, 10, 18, 21, 14, 16, 13, 19, 25]

plt.boxplot(data)
plt.title("Basic Boxplot")
plt.ylabel("Values")
plt.show()
