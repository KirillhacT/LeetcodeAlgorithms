# m - targetSum n - array Lenght
#O(n ^ m * m) -> O(m ^ 2 * n)
#O(m ^ 2) -> O(m^2)

def badBestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest_combination = None
    for i in numbers:
        remaind = targetSum - i
        res = badBestSum(remaind, numbers)
        if res != None:
            comp = res + [i]
            if not shortest_combination or len(comp) < len(shortest_combination):
                shortest_combination = comp
    return shortest_combination
# print(badBestSum(7, [5, 3, 4, 7]))

memo = {}
def goodBestSum(targetSum, numbers):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest_combination = None
    for i in numbers:
        remaind = targetSum - i
        res = goodBestSum(remaind, numbers)
        if res != None:
            comp = res + [i]
            if not shortest_combination or len(comp) < len(shortest_combination):
                shortest_combination = comp
    memo[targetSum] = shortest_combination
    return shortest_combination
print(goodBestSum(100, [1, 2, 5, 25]))