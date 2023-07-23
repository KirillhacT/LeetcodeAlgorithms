#O(2 ^ n + m) -> O(m * n)
#O(n + m) -> O(n + m)
#gridTraveller(a, b) == gridTraveller(b, a)

def badGridTraveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return badGridTraveller(m - 1, n) + badGridTraveller(m, n - 1)

# print(badGridTraveller(2, 3))

memo = {}
def goodGridTraveller(m, n):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = goodGridTraveller(m - 1, n) + goodGridTraveller(m, n - 1)
    return memo[key]
print(goodGridTraveller(18, 18))



