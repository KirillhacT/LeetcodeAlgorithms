mas = [3, 1, 2, 4, 5, 8, 5, 1, 2, 3, 4, 31]
m = max(mas)

bnt = [0] * (m + 1)
for i in mas:
    bnt[i] += 1
# print(bnt)
index = 0
for j in range(len(bnt)):
    for k in range(bnt[j]):
        mas[index] = j
        index += 1
# print(mas)

mas = [(0, 2), (2, 1), (0, 1), (1, 1), (2, 1), (2, 0), (0, 2), (0, 0)]
m = 3
cnt = [0] * m
for i in mas:
    cnt[i[1]] += 1
#[2, 4, 2]
mas2 = [0] * len(mas)
index = 0
offset = 0
    



    


