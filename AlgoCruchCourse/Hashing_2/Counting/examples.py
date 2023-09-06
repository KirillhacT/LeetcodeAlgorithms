#Находим максимальную подстроку в которой не больше k различных символов
a = "eceba"
k = 2

left = ans = 0
curr = 0
hash = {}

for right in range(len(a)):
    if a[right] not in hash:
        hash[a[right]] = 0
    hash[a[right]] += 1
    while len(hash) > k:
        hash[a[left]] -= 1
        if hash[a[left]] == 0:
            del hash[a[left]]
        left += 1
    ans = max(ans, right - left + 1)
# print(ans)

#Возвращаем значения, содержащиеся во всех массивах по возростанию
nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
hash = {}
mas = []
for arr in nums:
    for x in arr:
        if x not in hash:
            hash[x] = 0
        hash[x] += 1
for key in hash:
    if hash[key] == len(nums):
        mas.append(key)
# print(sorted(mas))


from collections import defaultdict
nums = [1, 2, 1, 2, 1]
#[1, 3, 4, 6, 7]
# 3 - 0 => 3
# 4 - 1 => 3
# 6 - 3 => 3 x2
# 7 - 4 => 3

k = 3
counts = defaultdict(int)
counts[0] = 1
ans = curr = 0

for num in nums:
    curr += num #1, 3, 4, 6, 7
    ans += counts[curr - k] # 1-3=-2, 3-3=0, 4-3=1, 7-3=4
    counts[curr] += 1 #c[1] += 1, c[3] += 1, c[4] += 1, c[7] += 1
# print(dict(counts))
# print(ans)

nums = [1, 1, 2, 1, 1]
k = 3
counts = defaultdict(int)
counts[0] = 1
ans = curr = 0

for num in nums:
    curr += num % 2 # 1, 2, 2, 3, 4
    ans += counts[curr - k] # 1-3=-2, 2-3=-1, 2-3=-1, 3-3=0, 4-3=1
    counts[curr] += 1
print(dict(counts))
print(ans)













    
        
    
