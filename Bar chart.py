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
r_std = []  # 標準差在這
for i, j, k in zip(r1, r2, r3):
  arr = np.array([i, j, k])
  r_std.append(round(np.std(arr, ddof=1), 2))


group = ["Raw", "Boiled", "Heated"]
rate = [round((sum(r1)+sum(r2)+sum(r3))/60, 2), 0, 0]
std = [sum(r_std)/7]
std.extend([0, 0])


plt.bar(group, rate, color="green", yerr=std, tick_label=group, capsize=5)
plt.title("")

plt.ylabel("Rate of Oxygen Production.(ml/s)") 
plt.xlabel("Group")

plt.show()
