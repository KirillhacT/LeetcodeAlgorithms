# Находим максимальную длину субмассива, сумма которого <= k
nums = [1, 4, 6, 9, 0, 2, 1, 1]
k = 4

left = ans = summ = 0
for right in range(len(nums)):
    summ += nums[right]

    while summ > k:
        summ -= nums[left]
        left += 1
    
    ans = max(ans, right - left + 1)
# print(ans)


# Находим максимальную длину субмассива, содержащим только один ноль
nums = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1]

left = countZeroes = ans = 0
for right in range(len(nums)):
    if nums[right] == 0:
        countZeroes += 1

    while countZeroes > 1:
        if nums[left] == 0:
            countZeroes -= 1
        left += 1
    ans = max(ans, right - left + 1)
# print(ans)


# Число суб массивов, произведение которых < k
nums = [10, 5, 2, 6] 
k = 100


if k <= 1:
    exit(1)
left = ans = 0
curr = 1
for right in range(len(nums)):
    curr *= nums[right]
    while curr >= k:
        curr //= nums[left]
        left += 1
    ans += right - left + 1
# print(ans)


#Максимальная сумма подмассива длины k
nums = [1, 9, 3, 4, 7, 9, 1]
k = 4
left = summ = ans = 0

for right in range(len(nums)):
    summ += nums[right]

    while right - left + 1 > k:
        summ -= nums[left]
        left += 1
    
    ans = max(ans, summ)
# print(ans)


#Реализация предыдущей задачи с фиксированным окном
nums = [1, 9, 3, 4, 7, 9, 1]
# first_window = sum(nums[:4]) ---> 1 + 9 + 3 + 4 = 17
k = 4
summ = 0
for i in range(k):
    summ += nums[i]
ans = summ
for j in range(k, len(nums)):
    # 1) iter --->  17 + 7 - 1 = 23; 
    # 2) iter --->  23 - 9 + 9 = 23; 
    # 3) iter --->  23 + 1 - 3 = 21
    summ += nums[j] - nums[j - k] 
    ans = max(ans, summ)
print(ans)









