# R組(生的)數據

from matplotlib import pyplot as plt
import math

# 數據
time = [i for i in range(0,61,10)]
r1 = [0, 2, 5, 11, 15, 19, 22]
r2 = [0, 8, 15, 19, 22, 26, 31]
r3 = [0, 5, 15, 17.5, 24, 27, 32.5]
# 生成平均列表，並無條件取到小數點第二位，避免圖表太醜
r_average = [round((a+b+c)/3, 2) for a,b,c in zip(r1, r2, r3)] 


plt.plot(time, r1, "b-", label="R-1")
plt.plot(time, r2, "b-.", label="R-2")
plt.plot(time, r3, "b--", label="R-3")
plt.plot(time, r_average, "r-", marker="o", label="R-Average")

# 把標籤弄上去
for label, x_p, y_p in zip(r_average, r_average, time):
  plt.annotate(label,
               xy=(y_p, x_p),
               xytext=(2,-10),
               textcoords="offset points")


plt.legend(loc=9)
plt.title("Data of Raw Group")
plt.ylabel("Production of Oxygen (ml.)")
plt.xlabel("Time (sec.)")

plt.show()
