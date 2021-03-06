import numpy as np
import pandas as pd
import pandas.plotting as pdplot
import matplotlib.pyplot as plt

print(plt.style.available)

np.random.seed(123)

df = pd.DataFrame({"A": np.random.randn(365).cumsum(0), "B": np.random.randn(365).cumsum(0) + 20, "C": np.random.randn(365).cumsum(0) - 20}, index=pd.date_range("1/1/2017", periods=365))
df.head()

df.plot()


df.plot('A','B', kind='scatter')

df.plot.scatter("A", "C", c="B", colormap="viridis")

ax = df.plot.scatter("A", "C", c="B", s=df["B"], colormap="viridis")
ax.set_aspect("equal")

df.plot.box()
df.plot.hist(alpha=0.7)
df.plot.kde()

iris = pd.read_csv("iris.csv")
print(iris.head())

pdplot.scatter_matrix(iris)

plt.figure()

pdplot.parallel_coordinates(iris, "Name")

plt.show()
