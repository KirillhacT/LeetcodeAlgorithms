#O(n * m)
#O(m)
def canSum(n, nums):
    mas = [False] * (n + 1)
    mas[0] = True
    for i in range(n + 1):
        if mas[i]:
            for j in nums:
                if j + i <= n:
                    mas[i + j] = True
    return mas[n]
print(canSum(7, [5, 3, 4]))







