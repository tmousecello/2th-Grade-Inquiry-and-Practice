# 表格

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
  r_std.append(round(np.std(arr, ddof=1)))

# 表格

r1.insert(0, "Raw - 1")
r2.insert(0, "Raw - 2")
r3.insert(0, "Raw - 3")
r_average.insert(0, "Raw - av")
b1.insert(0, "Boiled - 1")
b2.insert(0, "Boiled - 2")
b3.insert(0, "Boiled - 3")
b_average.insert(0, "Boiled - av")
h1.insert(0, "Heated - 1")
h2.insert(0, "Heated - 2")
h3.insert(0, "Heated - 3")
h_average.insert(0, "Heated - av")
r_std.insert(0, "Raw - stdv")
b_std = ["Boiled - stdv",0,0,0,0,0,0,0]
h_std = ["Heated - stdv",0,0,0,0,0,0,0]


sheet = [
         ["time(sec.)", 0, 10, 20, 30, 40, 50, 60],
         r1,
         r2,
         r3,
         r_average,
         r_std,
         b1,
         b2,
         b3,
         b_average,
         b_std,
         h1,
         h2,
         h3,
         h_average,
         h_std,
         ]

print(pd.DataFrame(sheet))

print("\n------------------------------------------------------------------------\n")

# 分開的表格
r_sheet = [
         ["time(sec.)", 0, 10, 20, 30, 40, 50, 60],
         r1,
         r2,
         r3,
         r_average,
         r_std,        
         ]
print(pd.DataFrame(r_sheet))
print("\n------------------------------------------------------------------------\n")

b_sheet = [
         ["time(sec.)", 0, 10, 20, 30, 40, 50, 60],
         b1,
         b2,
         b3,
         b_average,
         b_std,
         ]
print(pd.DataFrame(b_sheet))
print("\n------------------------------------------------------------------------\n")

h_sheet = [
         ["time(sec.)", 0, 10, 20, 30, 40, 50, 60],
         h1,
         h2,
         h3,
         h_average,
         h_std,
         ]
print(pd.DataFrame(h_sheet))
