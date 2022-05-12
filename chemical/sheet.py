# 數據

vinegar1 = [68, 67, 70]
vinegar2 = [77.4, 82.7, 73.3]
salt = [2, -1, 5]
soda = [2, 1, 0]
vinegar1.append(round(sum(vinegar1)/len(vinegar1), 2))
vinegar1.append(round(np.std(vinegar1, ddof=1), 2))
vinegar2.append(round(sum(vinegar2)/len(vinegar2), 2))
vinegar2.append(round(np.std(vinegar2, ddof=1), 2))
salt.append(round(sum(salt)/len(salt), 2))
salt.append(round(np.std(salt, ddof=1), 2))
soda.append(round(sum(soda)/len(soda), 2))
soda.append(round(np.std(soda, ddof=1), 2))
vinegar1.insert(0, "白醋一")
vinegar2.insert(0, "白醋二")
salt.insert(0, "食鹽")
soda.insert(0, "小蘇打")

# 讓他對齊
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)

# 畫表格
sheet = [
         ["組別", "實驗數據1", "實驗數據2", "實驗數據3", "平均", "標準差"],
         vinegar1, 
         vinegar2,
         salt,
         soda
         ]

print(pd.DataFrame(sheet))
