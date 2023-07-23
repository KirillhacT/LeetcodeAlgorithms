# m - targetSum n - array Lenght
#O(n ^ m) -> O(m * n)
#O(m) -> O(m)
def badCanSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remaind = targetSum - num
        if badCanSum(remaind, numbers):
            return True
    return False
# print(badСanSum(7, [2, 4]))


memo = {}
def goodCanSum(targetSum, numbers):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remaind = targetSum - num
        if goodCanSum(remaind, numbers):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False
print(goodCanSum(300, [7, 15]))



