# nums = [1, 2, 3, 4]
#
# mas = [1] * len(nums)
# for i in range(1, len(nums)):
#     mas[i] = mas[i - 1] * nums[i - 1]
# cur = 1
# print(mas)
# for j in range(len(nums)-2, -1, -1):
#     cur *= nums[j + 1]
#     mas[j] *= cur
# print(mas)



# 424. Longest Repeating Character Replacement
s = "ABAB"
hash = {}
k = 2
l = 0
res = 0
for r in range(len(s)):
    hash[s[r]] = 1 + hash.get(s[r], 0)
    # if s[r] not in hash:
    #     hash[s[r]] = 0
    # hash[s[r]] += 1
    maxHashValue = max(list(hash.values()))
    curLen = (r - l + 1) - maxHashValue
    if curLen > k:
        hash[s[l]] -= 1
        l += 1
        continue
    else:
        res = max(res, r - l + 1)
# print(res)


# n = int(input())
# a = list(map(int, input().split()))
#Задача с расстояниями от числа до ближайшего нуля
n = 8
a = [0, 1, 2, 5, 0, 5, 3, 0]
result = [n] * n
last_zero_pos = -n
for i in range(n):
    if a[i] == 0:
        last_zero_pos = i
    result[i] = min(result[i], i - last_zero_pos)
# print(result)
last_zero_pos = 2 * n
for i in range(n-1, -1, -1):
    if a[i] == 0:
        last_zero_pos = i
    result[i] = min(result[i], last_zero_pos - i)
# print(*result)


# #567. Permutation in String
# s1 = "ab"
# s2 = "eidbaooo"
# s1Count, s2Count = [0] * 26, [0] * 26
# for i in range(len(s1)):
#     #ord(s1[i])-ord('a') -> возвращает индекс, который соответствует месту в массиве под текущую букву
#     s1Count[ord(s1[i]) - ord('a')] += 1
#     s2Count[ord(s2[i]) - ord('a')] += 1
# matches = 0
# print(s1Count)
# print(s2Count)
# for i in range(26):
#     matches += (1 if s1Count[i] == s2Count[i] else 0)
# l = 0
# for r in range(len(s1), len(s2)):
#     if matches == 26:
#         print(True)
#         exit()
#     index = ord(s2[r]) - ord('a')
#     s2Count[index] += 1
#     if s1Count[index] == s2Count[index]:
#         matches += 1
#     elif s1Count[index] + 1 == s2Count[index]:
#         matches -= 1
#     index = ord(s2[l]) - ord('a')
#     s2Count[index] -= 1
#     if s1Count[index] == s2Count[index]:
#         matches += 1
#     elif s1Count[index] - 1 == s2Count[index]:
#         matches -= 1
#     l += 1
# print(matches == 26)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prv
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# from random import randint
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 4
# print(nums)
# curSum = 0
# for i in range(k):
#     curSum += nums[i]
# maxSub = curSum / 4
# for j in range(1, len(nums) - k + 1):
#     # if j + k > len(nums):
#     #     break
#     curSum = curSum - nums[j - 1] + nums[j + k - 1]
#     maxSub = max(maxSub, curSum)
# print(maxSub)


# nums = [4,2,0,3,2,5]
#
# l, r = 0, len(nums) - 1
# leftMax = nums[l]
# rightMax = nums[r]
# res = 0
#
# while l < r:
#     if leftMax < rightMax:
#         l += 1
#         leftMax = max(leftMax, nums[l])
#         res += leftMax - nums[l]
#     else:
#         r -= 1
#         rightMax = max(rightMax, nums[r])
#         res += rightMax - nums[r]
# print(res)

nums = [1, 2, 3]
res = []


subset = []
def dfs(i):
    if i >= len(nums):
        res.append(subset.copy())
        return
    subset.append(nums[i])
    dfs(i + 1)
    subset.pop()
    dfs(i + 1)
dfs(0)
print(res)






















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































