#O(m ^ 2 * n)
#O(m ^ 2)
def howSum(n, nums):
    mas = [None] * (n + 1)
    mas[0] = list()
    for i in range(n + 1):
        if mas[i] != None:
            for num in nums:
                if i + num <= n:
                    mas[i + num] = mas[i] + [num]
    return mas[n]




print(howSum(300, [7, 15]))