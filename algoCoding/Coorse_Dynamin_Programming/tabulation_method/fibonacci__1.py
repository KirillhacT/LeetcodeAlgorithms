def fib(n):
    mas = [0] * (n + 1)
    mas[1] = 1
    for i in range(n + 1):
        if i + 1 <= n:
            mas[i + 1] += mas[i]
        if i + 2 <= n:
            mas[i + 2] += mas[i]
    return mas[n]

    # mas = [0] * (n + 1)
    # mas[1] = 1
    # for i in range(2, n + 1):
    #     mas[i] = mas[i - 1] + mas[i - 2]
    # return mas[n]




print(fib(5))