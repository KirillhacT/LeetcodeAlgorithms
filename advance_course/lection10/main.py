#1
n = 10
mas = [1, 1] + [0] * (n - 2)
for i in range(2, n):
    mas[i] = mas[i - 1] + mas[i - 2]
print(mas)

n = 10
k = 2
mas = [0] * n
mas[0] = 1 
for i in range(1, n):
    for j in range(k):
        if i - j >= 0:
            mas[i] += mas[i - j - 1]
print(mas)
