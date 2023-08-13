#Простой пример с нахождением сумм на подмассиве
nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
out = []

prefix = [nums[0]] + [0] * (len(nums) - 1)
for i in range(1, len(nums)):
    prefix[i] = nums[i] + prefix[i - 1]
for mas in queries:
    i = mas[0]
    j = mas[1]
    boolean = (prefix[j] - prefix[i] + nums[i]) <= limit
    out.append(boolean)
# print(out)


#Кол-во способов разбить подмассив, где сумма первого больше суммы второго
nums = [10, 4, -8, 7]
ans = 0

prefix = [nums[0]] + [0] * (len(nums) - 1)
for i in range(1, len(nums)):
    prefix[i] = nums[i] + prefix[i - 1]
for i in range(len(nums)-1):
    left_section = prefix[i] #i element
    right_section = prefix[len(nums)-1] #last element
    #Если сумма левого подмассива больше суммы правого (не учитывая суммы левого в нем)
    # то считаем, что сумма левого подмассива больше правого
    if left_section >= right_section - left_section:
        ans += 1
# print(ans)


#Предыдущий пример без использования массива
nums = [10, 4, -8, 7]

ans = left_section = 0
total = sum(nums)
for i in range(len(nums)-1):
    left_section += nums[i]
    right_section = total - left_section
    if left_section >= right_section:
        ans += 1
print(ans)





