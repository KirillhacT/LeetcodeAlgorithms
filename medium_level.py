#dp - максимально выгодная продажа и покупка
from collections import Counter, defaultdict
from pprint import pprint

prices = [7,1,5,3,6,4]
dp = [0] * len(prices)
min_price = prices[0]

for i in range(1, len(prices)):
    min_price = min(min_price, prices[i])
    dp[i] = max(dp[i - 1], prices[i] - min_price)
# print(dp[-1])



#array - массив с суммой всех чисел не считая самого числа
nums = [-1, 1, 0, -3, 3]
# nums = [1,2,3,4]
answer = [0] * len(nums)
d = 1
# c_0 = len(nums) + 1
null = 1
flag = True
for i in range(len(nums)):
    if nums[i] == 0 and flag:
        null = 0
        flag = False
        continue
    d *= nums[i]

for i in range(len(nums)):
    if nums[i] == 0:
        answer[i] = d
    else:
        answer[i] = (d // nums[i]) * null
# print(answer)
#Лучшее решение
#Суть алгоритма - мы записываем префиксное произведение чисел
# с начала и до конца не считая последнего и префиксное
# произведение с конца до начала
nums = [1,2,3,4]
# ans = [1]
ans = [1] * len(nums)
for i in range(1, len(nums)):
    # ans.append(ans[-1] * nums[i - 1])
    ans[i] = ans[i - 1] * nums[i - 1]
# print(ans)
cur = 1
for i in range(len(nums)-2, -1, -1):
    cur *= nums[i + 1]
    # print(cur, end=" ")
    ans[i] *= cur
# print(ans)


#Two Pointers
s = "babad"
ans = ""
def Palindrome(ans, n):
    #Функция бежит тремя указателями
    """
    Первый указывает на элемент перед текущим
    Второй на сам элемент
    Третий указывает на следующий после текущего

    Если первый и третий элементы равны, то
    понижаем один и увеличиваем второй
    Таким образом находится длиннейший палиндром

    Функцию мы вызываем два раза (для четных и нечетных палиндромов)
    bab и abba
    """
    l, r = i, i + n
    while l >= 0 and r < len(s) and l <= r:
        if s[l] != s[r]:
            break
        if r - l + 1 > len(ans):
            ans = s[l:r + 1]
        l -= 1
        r += 1
    return ans
for i in range(len(s)):
    ans = Palindrome(ans, 0)
    ans = Palindrome(ans, 1)
# print(ans)


#Palindrome Linked List
"""
1) Найти середину 
2) Развернуть вторую половину
3) Проверка на палиндром
"""


#dp - Coin Change - минимальное кол-во монет, чтобы дать сдачу
coins = [1, 2, 5]
amount = 110

memo = {}
def helper(amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    if amount in memo:
        return memo[amount]
    c_min = float("inf")
    for i in coins:
        c_min = min(c_min, helper(amount - i) + 1)
    memo[amount] = c_min
    return c_min
# print(helper(amount))


#Two Pointers


#hash
strs = ["eat","tea","tan","ate","nat","bat"]
d = defaultdict(list)
# print(d)
for s in strs:
    key = tuple(sorted(s))
    # print(key)
    d[key].append(s)
# print(d.values())


#dp - Jump Game
nums = [2,3,1,1,4]
target = len(nums) - 1

for i in range(len(nums) - 2, -1, -1):
    if i + nums[i] >= target:
        target = i

# print(target == 0)


#dp - длина до последнего элемента в матрице
m = 3
n = 7
dp = [[0] * n for _ in range(m)]
# print(dp)
for row in range(m):
    for c in range(n):
        if row == 0 or c == 0:
            dp[row][c] = 1
            continue
        dp[row][c] = dp[row-1][c] + dp[row][c-1]
# print(dp[-1][-1])


#dp - подсчитываем максимальную прибыль покупок и продаж в разные дни
prices = [1,2,3,4,5]
ans = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
# print(ans)


#dp
from functools import lru_cache
s = "leetcode"
wordList = ["leet", "code"]
@lru_cache(None)
def helper_word(s):
    if not s:
        return True
    for w in wordList:
        lw = len(w)
        if w == s[:lw]:
            if helper_word(s[lw:]):
                return True
    return False
# print(helper_word(s))

#dp решение
dp = [False] * (len(s) + 1)
dp[-1] = True
for i in range(len(s)-1, -1, -1):
    for w in wordList:
        lw = len(w)
        p = s[i:i+lw]
        if len(w) <= len(s) - i and s[i:i+lw] == w:
            dp[i] = max(dp[i], dp[i+lw])
# print(dp[0])



#backtracking
ans = []
nums = [1, 2, 3]
def helper_back(i, subset):
    # print(subset)
    ans.append(subset[:])
    if i < len(nums):
        for j in range(i, len(nums)):
            subset.append(nums[j])
            helper_back(j+1, subset)
            subset.pop()
helper_back(0, [])
# print(ans)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="  ")
        print()
    print()


#matrix
matrix = [[1,1,1],[1,0,1],[1,1,1]]
# print_matrix(matrix)
first_col = False
m, n = len(matrix), len(matrix[0])
#Первыми двумя циклами бежим по матрице и выставляем ноли в столбцах, для дальнейшего решение
for r in range(m):
    if matrix[r][0] == 0:
        first_col = True
    for c in range(1, n):
        if matrix[r][c] == 0:
            matrix[0][c] = 0
            matrix[r][0] = 0
# print_matrix(matrix)
# print(first_col)
for r in range(1, m):
    for c in range(1, n):
        if matrix[0][c] == 0 or matrix[r][0] == 0:
            matrix[r][c] = 0
if matrix[0][0] == 0:
    for c in range(n):
        matrix[0][c] = 0
if first_col:
    for r in range(m):
        matrix[r][0] = 0


#binary search - ищем минимальный элемент в сдвинутом массиве
# nums = [3,4,5,1,2]
# if len(nums) < 2:
#     print(nums[0])
#
# l, r = 0, len(nums) - 1
# if nums[l] < nums[r]:
#     print(nums[l])
# while l <= r:
#     mid = (l + r) // 2
#     if nums[mid] > nums[mid + 1]:
#         print(nums[mid + 1])
#     if nums[mid] > nums[r]:
#         l = mid + 1
#     else:
#         r = mid


#Jump Game II
nums = [2,3,1,1,4]
@lru_cache(None)
def helper(i):
    if i >= len(nums)-1:
        return 0
    ans = float("inf")
    for j in range(1, nums[i]+1):
        ans = min(ans, helper(i + j) + 1)
    return ans
# print(helper(0))


#Rotate Array
"""
nums = [1,2,3,4,5,6,7], k = 2
1) Разворачиваем полностью массив -> [7, 6, 5, 4, 3, 2, 1]
2) меняем первые k элементов (6 и 7) -> [6, 7, 5, 4, 3, 2, 1]
3) меняем местами все элементы после k -> [6, 7, 1, 2, 3, 4, 5]"""

nums = [1,2,3,4,5,6,7]
k = 3
def rev(l, r):
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
n = len(nums)
rev(0, n - 1)
rev(0, k % n - 1)
rev(k % n, n - 1)
# print(nums)


#17. Letter Combinations of a Phone Number
digits = "234"
d = {"2": 'abc',
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
# if digits == '':
#     print([])
ans = []
def dfs(i, comb):
    if i == len(digits):
        ans.append(comb)
        return
    for l in d[digits[i]]:
        dfs(i+1, comb+l)
dfs(0, "")
# print(ans)


#138. Copy List with Random Pointer
#Linked List


#3. Longest Substring Without Repeating Characters
#Sliding Window
s = "abcabcbb"
d = {}
i = 0
ans = 0
for j in range(len(s)):
    if s[j] in d:
        i = max(d[s[j]] + 1, i)
    d[s[j]] = j
    ans = max(ans, j - i + 1)
# print(ans)


#Rotate List


#207. Course Schedule
#DFS
numCourses = 2
# prerequisites = [[1,0]]
prerequisites = [[1,0],[0,1]]
graph = [[] for _ in range(numCourses)]
for c, prereq in prerequisites:
    graph[c].append(prereq)
def dfs(i):
    if not graph[i]:
        return False
    if i in visited:
        return True
    visited.add(i)
    for j in graph[i]:

        if dfs(j):
            return True
    visited.remove(i)
    return False
for i in range(numCourses):
    visited = set()
    if dfs(i):
        pass
        # print(False)
    else:
        graph[i] = []
# print(True)


#Unique Path II
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
m, n = len(obstacleGrid), len(obstacleGrid[0])
dp = [[0] * n for _ in range(m)]
#Проставляем нули в первом столбце и ряде, если там есть препятствие
for c in range(n):
    if obstacleGrid[0][c] == 1:
        break
    dp[0][c] = 1
for r in range(m):
    if obstacleGrid[r][0] == 1:
        break
    dp[r][0] = 1

for r in range(1, m):
    for c in range(1, n):
        if obstacleGrid[r][c] == 0:
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
# print(dp[-1][-1])


#Combination Sum
#Backtracking
ans = []
candidates = [2, 3, 6, 7]
target = 7
def dfs(i, sum, comb):
    if sum == 0:
        ans.append(comb)
        return
    if sum < 0:
        return
    for j in range(i, len(candidates)):
        dfs(j, sum-candidates[j], comb+[candidates[j]])
dfs(0, target, [])
# print(ans)

# 54. Spiral Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
d = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}
m, n = len(matrix), len(matrix[0])
ans = []

r, c = 0, 0
dirr = (0, 1)
for _ in range(m * n):
    ans.append(matrix[r][c])
    matrix[r][c] = "#"
    rs, cs = dirr
    nr, nc = r + rs, c + cs
    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != "#":
        r, c = nr, nc
    else:
        dirr = d[dirr]
        rs, cs = dirr
        r, c = r + rs, c + cs
# print(ans)


#Rotate Image
"""
1) Инвертировать строки
2) Транспонировать
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
l, r = 0, n-1
while l <= r:
    matrix[l], matrix[r] = matrix[r], matrix[l]
    l += 1
    r -= 1
for r in range(n):
    for c in range(r, n):
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
# print(matrix)

#53. Maximum Subarray
#dp
nums = [-2,1,-3,4,-1,2,1,-5,4]
dp = [0] * len(nums)
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])
    # print(max(dp))

nums = [1,1,1,2,2,3, 3, 3, 3]
hash = {}
for key in nums:
    if key not in hash:
        hash[key] = 0
    hash[key] += 1
# print(hash)
ans = sorted(hash, key=hash.get, reverse=True)
# print(ans)


class MinStack:
    def __init__(self):
        self.mas = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.mas.append(val)

    def pop(self) -> None:
        a = self.mas.pop()
        if a == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.mas[-1]

    def getMin(self) -> int:
        return self.min[-1]

string = "abcabacabcabz"
hash = set()
maxLen = 0
l = 0
for r in range(len(string)):
    while string[r] in hash:
        hash.remove(string[l])
        l += 1
    hash.add(string[r])
    maxLen = max(maxLen, r - l + 1)
# print(maxLen)

count = 0
nums = [-1,2,1,-4]
target = 1

nums.sort()
for i in range(len(nums)):
    if i < 0 and nums[i] == nums[i - 1]:
        continue
    l, r = i + 1, len(nums)-1
    while l < r:
        if i == l or r == len(nums):
            break
        cur = nums[i] + nums[l] + nums[r]
        if cur > target:
            r -= 1
        elif cur < target:
            l += 1
        else:
            count += 1
            l += 1
            while l < r and nums[i] == nums[i - 1]:
                l += 1
print(count)































