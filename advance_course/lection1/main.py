a = [4, 1, 3, 5, 6]

for i in range(1, len(a) - 1):
    cur = i
    while cur > 0 and a[cur] < a[cur - 1]:
        a[cur], a[cur - 1] = a[cur - 1], a[cur]
        cur -= 1
print(a)
