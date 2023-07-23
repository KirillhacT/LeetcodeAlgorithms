# m - targetSum n - array Lenght
#O(n ^ m * m) -> O(m ^ 2 * n)
#O(m) -> O(m^2)

def badHowSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remaind = targetSum - num
        res = badHowSum(remaind, numbers)
        if res != None:
            res.append(num)
            return res
    return None


memo = {}
def goodHowSum(targetSum, numbers):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remaind = targetSum - num
        res = goodHowSum(remaind, numbers)
        if res != None:
            res.append(num)
            memo[targetSum] = res
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(goodHowSum(7, [5, 3, 3, 1]))
print(memo)

