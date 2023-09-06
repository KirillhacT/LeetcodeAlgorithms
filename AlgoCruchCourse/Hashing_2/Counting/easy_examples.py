""" Two Sum """
nums = [4, 1, 2, 5, 7, 8]
target = 6
hash = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in hash:
        # print(i, hash[diff])
        continue
    hash[nums[i]] = i


nums = [4, 1, 2, 5, 7, 8]
target = 6
hash = set()
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in hash:
        # print(nums[i], diff)
        continue
    hash.add(nums[i])


nums = [4, 1, 2, 5, 7, 8, 10]
mas = []
hash = set()

hash = set(nums)

for j in range(len(nums)):
    cur = nums[j]
    if cur - 1 not in hash and cur + 1 not in hash:
        mas.append(cur)
# print(mas) 


#managram
import string
str = "askdfiosdhfisahulifhlkewdgflyaWGLE;G;'F/HsU"
hash = set(string.ascii_lowercase)
for i in str:
    if i not in hash:
        # print(False)
        break

nums = [3, 0, 1]
hash = set(nums)
for i in range(len(nums) + 1):
    if i not in hash:
        print(i)
        break 






