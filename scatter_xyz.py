# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

from sklearn.cluster import DBSCAN


plot=False


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f = open("xyz.dat")
lines = f.readlines()[1:]
xs = []
ys = []
zs = []
xyzs = []
for line in lines:
    s = line.split()
    xs.append(float(s[1]))
    ys.append(float(s[2]))
    zs.append(float(s[3]))
    xyzs.append([float(s[1]), float(s[2]), float(s[3])])

clustering = DBSCAN(eps=1, min_samples=100).fit(xyzs)
c=list(clustering.labels_)


df = pd.DataFrame({"x": xs, "y":ys, "z": zs, "c":c})
df = df[df["c"] != -1]
df.to_csv("xenon_DBSCAN.csv", index=False)

if plot:
    ax.scatter(df.x, df.y, df.z, c=df.c)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
