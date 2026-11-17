import matplotlib.pyplot as plt

import pandas as pd

data = [12, 15, 14, 10, 18, 21, 14, 16, 13, 19, 25]

plt.boxplot(data)
plt.title("Basic Boxplot")
plt.ylabel("Values")
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
x+y
print(x+y)