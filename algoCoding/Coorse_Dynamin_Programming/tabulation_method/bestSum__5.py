#O(m ^ 2 * n)
#O(m ^ 2)
def bestSum(n, nums):
    mas = [None] * (n + 1)
    mas[0] = list()
    for i in range(n + 1):
        if mas[i] != None:
            for num in nums:
                if i + num <= n:
                    if mas[i + num] == None:
                        mas[i + num] = mas[i] + [num]
                    else:
                        if len(mas[i + num]) > len(mas[i] + [num]):
                            mas[i + num] = mas[i] + [num]


    return mas[n]


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4 ,5]))
print(bestSum(100, [1, 2, 5, 25]))
print(bestSum(11, [1, 2, 5]))