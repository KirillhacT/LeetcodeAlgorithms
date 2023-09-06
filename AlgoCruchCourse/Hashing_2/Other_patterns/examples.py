# Group Anagrams
strs = ["eat","tea","tan","ate","nat","bat"]
hash = {}

for word in strs:
    key = "".join(sorted(word))
    if key not in hash:
        hash[key] = []
    hash[key].append(word)
# print(list(hash.values()))


#pick up the same cards
from collections import defaultdict
cards = [1, 2, 6, 2, 1]
hash = defaultdict(list)
ans = float("inf")
for i in range(len(cards)):
    hash[cards[i]].append(i)

for key in hash:
    arr = hash[key]
    for index in range(1, len(arr)):
        ans = min(ans, arr[index] - arr[index - 1] + 1)
# print(h := ans if ans != float("inf") else -1)

#impoved decision
cards = [1, 2, 6, 2, 1]
hash = {}
ans = float("inf")
for i in range(len(cards)):
    if cards[i] in hash:
        ans = min(ans, i - hash[cards[i]] + 1)
    hash[cards[i]] = i
# print(h := ans if ans != float("inf") else -1)



#2342. Max Sum of Pair With Equal Sum of digits 
nums = [18, 43, 36, 13, 7]
hash = {}
ans = -1
for num in nums:
    summ = 0
    cur = num
    while cur:
        summ += cur % 10
        cur //= 10
    if summ not in hash:
        hash[summ] = []
    hash[summ].append(num)
for key in hash:
    hash[key].sort()
    arr = hash[key]
    if len(arr) > 1:
        ans = max(ans, arr[-1] + arr[-2])
# print(ans)

#improved decision
def get_digit_sum(num):
    digit_sum = 0
    while num:
        digit_sum += num % 10
        num //= 10
    
    return digit_sum

dic = defaultdict(int)
ans = -1
for num in nums:
    digit_sum = get_digit_sum(num)
    if digit_sum in dic:
        ans = max(ans, num + dic[digit_sum])
    dic[digit_sum] = max(dic[digit_sum], num)
# print(ans)



# 2352. Equal Row and Column Pairs
grid = [[3,2,1],[1,7,6],[2,7,7]]
hash_col = {}
hash_row = {}
count = 0
for i in grid:
    key = tuple(i)
    if key not in hash_row:
        hash_row[key] = 0
    hash_row[key] += 1
for i in range(len(grid)):
    mas = [0] * len(grid)
    for j in range(len(grid)):
        mas[j] = grid[j][i]
    key = tuple(mas)
    if key not in hash_col:
        hash_col[key] = 0
    hash_col[key] += 1
for key in hash_col:
    if key in hash_row:
        count += hash_row[key] * hash_col[key]
print(count)










