# nums = [5, 1, 4, 3, 9]
# prefixSum = [0] * (len(nums) + 1)
#
# for i in range(1, len(nums) + 1):
#     prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
# print(prefixSum)
#
# def rsq(prefixSum, l, r):
#     return prefixSum[r] - prefixSum[l]
# print(rsq(prefixSum, 0, 5))
#
#
# #Кол-во нулей на полуинтервале
# nums = [1, 0, 1, 1, 0, 0, 1, 0]
# prefixZeroes = [0] * (len(nums) + 1)
# for i in range(1, len(nums) + 1):
#     if nums[i - 1] == 0:
#         prefixZeroes[i] = prefixZeroes[i - 1] + 1
#     else:
#         prefixZeroes[i] = prefixZeroes[i - 1]
# print(prefixZeroes)
#
# def countZeroes(prefixzeroes, l, r):
#     return prefixzeroes[r] - prefixzeroes[l]


# nums = [-1, -2, 1, -1, -2, -2, 1, -2, 1, 2, -1, 2, 2]
# prefixSymValue = {0: 1}
# nowsum = 0
# for now in nums:
#     nowsum += now
#     if nowsum not in prefixSymValue:
#         prefixSymValue[nowsum] = 0
#     prefixSymValue[nowsum] += 1
# print(prefixSymValue)
# cntranges = 0
# for nowsum in prefixSymValue:
#     cntsum = prefixSymValue[nowsum]
#     cntranges += cntsum * (cntsum - 1) // 2
# print(cntranges)


#Два указателя
# nums = [1, 3, 5, 7, 8] #5-3=2, 5-4=1; 1 + 2 = 3
# k = 4
# count = 0
# last = 0
# for i in range(len(nums)):
#     while last < len(nums) and nums[last] - nums[i] <= k:
#         last += 1
#     count += len(nums) - last
# print(count)

numbers = [-1,0,1,2,-1,-4]
res = []

numbers.sort()
for i in range(len(numbers)):
    while numbers[i] == numbers[i + 1]:
        continue
    l, r = i + 1, len(numbers)-1
    while l < r:
        cur = numbers[i] + numbers[l] + numbers[r]
        if cur > 0:
            r -= 1
        elif cur < 0:
            l += 1
        else:
            res.append([numbers[i], numbers[l], numbers[r]])
            while numbers[l] == numbers[l - 1] and l < r:
                l += 1
























