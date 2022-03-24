# 全部數據

from matplotlib import pyplot as plt
import math
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# 數據
time = [i for i in range(0,61,10)]
r1 = [0, 2, 5, 11, 15, 19, 22]
r2 = [0, 8, 15, 19, 22, 26, 31]
r3 = [0, 5, 15, 17.5, 24, 27, 32.5]
r_average = [round((a+b+c)/3, 2) for a,b,c in zip(r1, r2, r3)] 
b1 = [0, 0, 0, 0, 0, 0, 0]
b2 = [0, 0, 0, 0, 0, 0, 0]
b3 = [0, 0, 0, 0, 0, 0, 0]
b_average = [round((a+b+c)/3, 2) for a,b,c in zip(b1, b2, b3)] 
h1 = [0, 0, 0, 0, 0, 0, 0]
h2 = [0, 0, 0, 0, 0, 0, 0]
h3 = [0, 0, 0, 0, 0, 0, 0]
h_average = [round((a+b+c)/3, 2) for a,b,c in zip(h1, h2, h3)] 

plt.plot(time, r1, "b:", label="R-1")
plt.plot(time, r2, "b-.", label="R-2")
plt.plot(time, r3, "b--", label="R-3")
plt.plot(time, r_average, "b-", marker="o", label="R-Average")
plt.plot(time, b1, "g:", label="B-1")
plt.plot(time, b2, "g-.", label="B-2")
plt.plot(time, b3, "g--", label="B-3")
plt.plot(time, b_average, "g-", marker="o", label="B-Average")
plt.plot(time, h1, "y:", label="H-1")
plt.plot(time, h2, "y-.", label="H-2")
plt.plot(time, h3, "y--", label="H-3")
plt.plot(time, h_average, "y-", marker="o", label="H-Average")

# 數據被一樣，就不標兩個數據了
for label, x_p, y_p in zip(r_average, r_average, time):
  plt.annotate(label,
               xy=(y_p, x_p),
               xytext=(2,-10),
               textcoords="offset points")
for label, x_p, y_p in zip(b_average, b_average, time):
  plt.annotate(label,
               xy=(y_p, x_p),
               xytext=(2,-10),
               textcoords="offset points")

plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title("Data of  All")
plt.ylabel("Production of Oxygen (ml.)")
plt.xlabel("Time (sec.)")

plt.show()
