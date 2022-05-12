# 數據

vinegar1 = [68, 67, 70]
vinegar2 = [77.4, 82.7, 73.3]
salt = [2, -1, 5]
soda = [2, 1, 0]

# 計算平均值與標準差
vinegar1_stdv = round(np.std(vinegar1, ddof=1), 2)
vinegar1_av = round(sum(vinegar1)/len(vinegar1))
vinegar2_stdv = round(np.std(vinegar2, ddof=1), 2)
vinegar2_av = round(sum(vinegar2)/len(vinegar2))
salt_stdv = round(np.std(salt, ddof=1), 2)
salt_av = round(sum(salt)/len(salt))
soda_stdv = round(np.std(soda, ddof=1), 2)
soda_av = round(sum(soda)/len(soda))

# 繪製長條圖
group = ["vinegar1", "vinegar2", "salt", "soda"]
rate = [vinegar1_av, vinegar2_av, salt_av, soda_av]
std = [vinegar1_stdv, vinegar2_stdv, salt_stdv, soda_stdv]

plt.bar(group, rate, color="green", yerr=std, tick_label=group, capsize=5)
plt.title("")

plt.ylabel("Precipitate weight.(g)") 
plt.xlabel("Group")

plt.show()
