
# matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# nums = [[], []]
# hash = {}

# for arr in matches:
#     for j in range(2):
#         if arr[j] not in hash:  
#             hash[arr[j]] = 0
#         if j == 1:
#             hash[arr[j]] -= 1

# for key in hash:
#     curr = hash[key]
#     if curr == 0:
#         nums[0].append(key)
#     elif curr == -1:
#         nums[1].append(key)
# nums[0].sort()
# nums[1].sort()
# print(nums)

#Largest Unique number
nums = [5, 7, 1, 9, 0, 3, 1, 9, 8, 3, 9, 7, 8]

hash = {}
for i in range(len(nums)):
    if nums[i] not in hash:
        hash[nums[i]] = 0
    hash[nums[i]] += 1
max_number = -1

for key in hash:
    if hash[key] == 1 and key > max_number:
        max_number = key
print(max_number)






