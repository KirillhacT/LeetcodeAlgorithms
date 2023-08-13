nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3

prefix = [nums[0]] + [0] * (len(nums) - 1)
for i in range(1, len(nums)): #Высчитываем префиксную сумму
    prefix[i] = prefix[i - 1] + nums[i] 

mas = [0] * len(nums)
for j in range(len(nums)):
    if j - k < 0 or j + k >= len(nums):
        mas[j] = -1
        continue
    prefix_start = j - k
    prefix_end = j + k
    summ = prefix[prefix_end] - prefix[prefix_start] + nums[prefix_start]
    mas[j] = summ // (prefix_end - prefix_start + 1)
print(mas)