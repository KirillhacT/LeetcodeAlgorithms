mas = [2, 5, 8, 12, 21, 27, 35]
x = 27
# l, r = 0, len(mas)-1
# while l <= r:
#     m = (l + r) // 2
#     val = mas[m]
#     if val == x:
#         print(m)
#         break
#     elif val > x:
#         r = m - 1
#     else:
#         l = m + 1

#Ищем минимальное число, которое либо равно х либо немного больше его
x = 24
l, r = -1, len(mas)
while r - l > 1:
    m = (l + r) // 2
    if mas[m] < x:
        l = m
    else:
        r = m
print(mas[r])

x = 9
l, r = -1, len(mas)
while r - l > 1:
    m = (l + r) // 2
    if mas[m] <= x:
        l = m
    else:
        r = m
print(mas[l])

def good(x):
    return (x // n) * (x // m) >= n

w, h, n = 2, 2, 10
l = 0
r = max(w, h) * n #max(w, h) * n^0,5
while r - l > 1:
    m = (l + r) // 2
    if good(m):
        r = m
    else:
        l = m
print(r)







