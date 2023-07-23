#Палиндром число (divmod)
import bisect

x = 456
if x < 0:
    print("Число не палиндром, потому что оно отрицательное")
orig = x
new = 0
while x:
    digit = x % 10
    x //= 10
    # x, digit = divmod(x, 10) #Эквивалент
    new = new * 10 + digit
    """0 * 10 + 6 = 6
    6 * 10 + 5 = 65
    65 * 10 + 4 = 654
    """
# print(new)


#set() - hash
a = [1, 2, 3, 1]
# print(len(a) != len(set(a))) #Определяем, встречается ли дубликат числа в массиве


#Linked List - СЛОЖНАААА


#bitmask
a1 = 3
b = a1 & 1 #Возвращает последнюю битовую цифру числа a % 2
a1 >>= 1 #Битовый сдвиг на один элемент влево - (1.1) a //= 1 * 10
# print(a, b)


#Удаление из емайла ненужных элементов
#Множество емайлов можно засунуть в set() для кол-ва уникальных
email = "test.email+alex@leetcode.com"
name, dom = email.split("@")
name = name.split("+")[0] #test.email
name = name.replace(".", "") #testemail
# print(f"{name}@{dom}")


#slinding window
#Перебор всех массивов неуместен (скорость N^2)
# q = deque([]) можно использовать двустороннюю очередь в качестве подмассива
nums = [1, 2, 3, 4, 5]; k = 1
ans = float('-inf') #-бесконечность
cnt = 0 #Счетчик, оповещающий что мы достигли элемента k
cur = 0 #Текущая сумма
for i in range(len(nums)):
    cur += nums[i]
    cnt += 1
    if cnt == k:
        ans = max(ans, cur/k)
    elif cnt > k:
        cur -= nums[i-k]
        ans = max(ans, cur/k)
# print(ans)


#two pointers
#Решаем задачу о переставлении нулей в конец списка с помощью двух указателей
a = [0, 1, 2, 0, 3, 4]
j = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]
        j += 1
# print(a)


#binary_searchif - проверяем, является ли число квадратом
#В данном случае мы перебираем бин поиском числа, которые могли бы быть квадратом нашего числа
num = 16
l, r = 1, num // 2 #от 1 до 8
while l <= r:
    mid = (l + r) // 2
    sq = mid * mid
    if sq == num:
        pass
        # print("yes")
    if sq < num:
        l = mid + 1
    else:
        r = mid - 1

#divmod
#Пытаемся сделать из числа однозначное, используя divmod с повтором
num = 10
while num >= 10:
    cur = num
    new_num = 0
    while cur:
        new_num += cur % 10
        cur //= 10
    num = new_num
# print(num)

#string
s = "PPALLP"
# return s.count("A") < 2 and s.count("LLL") == 0
#count - наше все


#Binary Tree - СЛОЖНАА


#stack проверяем на соответствие строки шаблону
s1 = "abc"
t1 = "ahbgdc"
stack = list(s1)[::-1] #cba

for c in t1:
    if stack and stack[-1] == c:
        stack.pop() #cba cb c; так как and ленивый, мы не возьмем элемент из пустого массива
# print(len(stack) == 0)

#binary tree - ну такое


#divmod Прибавление еденицы к массиву
carry = 1
digits = [1, 2, 3]
for i in range(len(digits)-1, -1, -1):
    carry, digits[i] = divmod(digits[i]+carry, 10)
digits = digits if not carry else [carry] + digits
# print(digits)

#sorting - meeting rooms (заблокировано)
intervals = [[7, 10], [2, 4]]
intervals.sort()
for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i-1][1]:
        print("No")
        exit()
# print("Yes")


#Linked List - ...


#hash Проверка, есть ли в два числа в массиве такие, что произведение одного из них на 2 равно другому
# arr = [0, 0]
# hash = {}
# count_0 = 0
# for i, j in enumerate(arr):
#     if j == 0:
#         count_0 += 1
#         if count_0 == 2:
#             print("Yes")
#     hash[j] = i
# for i in hash:
#     cur_num = i * 2
#     if cur_num in hash and cur_num != 0:
#         print(cur_num)
#         print("Yes")
# print("No")
hash = set()
arr = [10,2,5,3]
for num in arr:
    if num * 2 in hash or num / 2 in hash:
        pass
        # print("Yes")
        # exit()
    hash.add(num)
# print("No")


#dp - Tribonacci
n = 4
T = [0, 1, 1] + [0] * (n - 2)
for i in range(3, n + 1):
    T[i] = T[i-1] + T[i-2] + T[i-3]
# print(T)


#dp - Треугольник паскаля
n = 5
dp = [[1], [1, 1]] #[1, 2, 1] [1, 3, 3, 1]
if n < 3:
    print(dp[:n])
for _ in range(n-2):
    len_cur_row = len(dp[-1])
    next_row = [1] + [0] * len_cur_row #[1, 0, 0] [1, 0, 0, 0]
    for i in range(1, len_cur_row):
        #от 1 до длины последнего (2) (3)
        # next_row.append(dp[-1][i] + dp[-1][i-1])
        next_row[i] = dp[-1][i] + dp[-1][i - 1]
        #1 + 1 -> 2; 1 + 2 -> 3, 2 + 1 -> 3
    next_row[-1] = 1
    dp.append(next_row)
# print(dp)
#Треугольник паскаля 2, находим ряд чисел по индексу
# mas = [[1], [1, 1]]
# rowIndex = 5
# if rowIndex < 2:
#     print(mas[rowIndex])
#     exit()
# for _ in range(1, rowIndex):
#     cur_row = [1]
#     for i in range(1, len(mas[-1])):
#         cur_row.append(mas[-1][i] + mas[-1][i-1])
#     cur_row += [1]
#     mas.append(cur_row)
# print(mas[rowIndex])


#bitmask - вывести число, единожды встречающееся в массиве
a = [4,1,2,1,2]
cur = 0
for i in a:
    cur ^= i
    # print(cur)

#binary_search - находим гору в массиве
#Заметка по bin поиску, если условие не проходит, то можно
#Сделать проверку границ нестрогой, убрать единицы при делении пополам, возвращаем либо правую либо левую границу
arr = [0,10,5,2]
l, r = 0, len(arr)-1
while l <= r:
    mid = (l + r) // 2
    if arr[mid - 1] < arr[mid] > arr[mid + 1]:
        break
        # print(mid)
        # exit()
    if arr[mid - 1] < arr[mid] < arr[mid + 1]:
        l = mid
    else:
        r = mid


#string вычисляем корректный палиндром без учета знаков и цифр
s = "A man, a plan, a canal: Panama"
l, r = 0, len(s) - 1
while l <= r:
    if not s[l].isalnum():
        l += 1
        continue
    if not s[r].isalnum():
        r -= 1
        continue
    if s[l].lower() != s[r].lower():
        break
        # print("No")
        # exit()
    l += 1
    r -= 1
# print("True")

#string - переворот массива строк

s = ["h", "e", "l", "l", "o", "f"]
i = 0
j = len(s) - 1
while i <= j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
# print(s)

#binary search - поиск квадрата числа или ближайшего к нему
if x < 2:
    pass
    # print(x)
l, r = 0, x // 2
while l <= r:
    mid_number = (l + r) // 2
    if mid_number * mid_number == x:
        pass
        # print(mid_number)
    if mid_number * mid_number < x:
        l = mid_number + 1
    else:
        r = mid_number - 1
# print(r) #Строго возвращаем правую границу

#hash - вычисляем букву, добавленную в строку в произвольном месте
from collections import Counter
strq = "a"
tq = "aa"
# print(list((Counter(tq) - Counter(strq)).elements())[0])


#stack - удаляем зеркально повторяющиеся числа
s = "aababaab"
s1 = "azxxzy"
stack = list()
for i in s1:
    if stack:
        if stack[-1] == i:
            stack.pop()
            continue
    stack.append(i)
# print(stack)


#Two pointers - Переворот каждого слова в предложении
s = "Egor Egor"
# new_s = " ".join([i[::-1] for i in s.split(" ")])
# print(new_s)
words = s.split(" ")
for index, word in enumerate(words):
    i = len(word) - 1
    new_str = ""
    while i >= 0:
        # word[i], word[j] = word[j], word[i]
        new_str += word[i]
        i -= 1
    words[index] = new_str
# print(words)


#binary search - ищем в массиве чисел позицию заданного числа
nums = [1, 3, 5, 6]
target = 5
result = bisect.bisect_left(nums, target)
# print(result)


#math - определяем, является ли число n степенью числа k
n = 625
k = 5
while n != 1:
    if n < 1:
        pass
        # print("No")
        # exit()
    n /= k
# print("Yes")
#Реализация рекурсией
def isPowerNumber(n, p) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    return isPowerNumber(n / p, p)
# print(isPowerNumber(16, 4))


#hash
"""Если задачу можно решить с помощью словаря, то проще ее можно 
   решить с помощью коллекции Counter"""
s = "anagram"
t = "nagaram"
c1 = Counter(s)
t1 = Counter(t)
# print(c1 == t1)


#array - вычисляем, можем ли мы поставить в массив нек. кол-во единиц так, чтобы они повторялись через 1
flowerbed = [1, 0, 0, 0, 1]
flowerbed = [0] + flowerbed + [0]
n = 1
for i in range(1, len(flowerbed)-1):
    if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        flowerbed[i] = 1
        n -= 1
# print(n <= 0)


#Binary Tree


#stack проверяем две строки на равенство с учетом символа стирания - решетки
s = "ab#c"
t = "ad#c"
def typing(s):
    stack = []
    for i in s:
        if i == "#":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
# print(typing(s) == typing(t))


#Linked List


#math является ли число степенью двойки
n = 16
if n == 0:
    pass
    # print("No")
    # exit()
while n % 2 == 0:
    n //= 2
# print(n == 1)


#Linked List


#bitwice
x = 1
y = 4
ans = 0
while x or y:
    ans += (x & 1) != (y & 1)
    x >>= 1
    y >>= 1
# print(ans)

nums = [9,6,4,2,3,5,7,0,1]
ran = set(range(len(nums)+1))
# print(ran)
st = list(ran - set(nums))[0]
# print(st)


#two pointers
#Переворачиваем каждый массив и инвертируем числа
image = [[1,1,0],[1,0,1],[0,0,0]]
for row in image:
    l, r = 0, len(row) - 1
    while l <= r:
        row[l], row[r] = row[r], row[l]
        row[l] = 0 if row[l] else 1
        if l != r:
            row[r] = 0 if row[r] else 1
        l += 1
        r -= 1
# print(image)


#Two pointers
#Ищем два числа в массиве, в сумме дающих target и возвращаем индексы на них
#Наивное решение
# hash = {}
# for i in range(len(numbers)):
#     hash[numbers[i]] = i

# for i, j in enumerate(numbers):
#     dr = target - j
#     if dr in hash and hash[dr] != i:
#         return [i + 1, hash[dr] + 1]
#Крутое решение (Благодаря тому, что массив отсортирован)
# numbers = [2, 7, 11, 15]
# target = 9
# l, r = 0, len(numbers) - 1
# while l <= r:
#     cur = numbers[l] + numbers[r]
#     if cur == target:
#         print([l + 1, r + 1])
#     if cur > target:
#         r -= 1
#     else:
#         l += 1

#hash
#Задача оставется не законченной
#Прием, докидываем хешей в пустрое пространство, чтобы уравнять массивы
"""
if len(w1) < len(w2):
    w1 += '#' * (l2 - l1)
else:
    w2 += '#' * (l1 - l2)
"""
words = ["app","apple"]
order = "abcdefghijklmnopqrstuvwxyz"
if len(words) < 2:
    print(True)
hash = {c:i for i, c in enumerate(order)}
# print(hash)
for k in range(1, len(words)):
    word1 = words[k - 1]
    word2 = words[k]
    l1, l2 = len(word1), len(word2)
    i = 0
    j = 0
    while i < l1 and j < l2:
        if hash[word1[i]] > hash[word2[j]]:
            pass
            # print(False)
        i += 1
        j += 1
    if l1 > l2:
        pass
        # print(False)
# print(True)


#array
# arr = [0, 3, 2, 1]
# i = 0
# if arr[i] > arr[i + 1] or arr[j] > arr[j - 1]:
#     pass
#     # print(False)
# while arr[i] > arr[j + 1]:
#     i += 1
# j = len(arr) - 1
# while arr[j] < arr[j - 1]:
#     j -= 1
# # print(i == j)


#math
s = "IX"
symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
ans = 0
i = 0
while i < len(s):
    #Если наш индекс не превышает последний элемент массива и
    #текущее значение символа меньше значения следующего
    if i < len(s) - 1 and symbols[s[i]] < symbols[s[i + 1]]:
        #Прибавляем к результату их разность (IV, IX, и т.д)
        #И перескакиваем на 2 еденицы
        ans += symbols[s[i + 1]] - symbols[s[i]]
        i += 2
    else:
        #Иначе прибавляем текущий символ и продвигаемся далее
        ans += symbols[s[i]]
        i += 1
# print(ans)



#string - задача о разбиении строки на подстроки, разделенные тире
# s = "5F3Z-2e-9-w"
# s = "2-4A0r7-4k"
# k = 3
# s = s.replace("-", "").upper()
# print(s)
# ost = len(s) % k
# min = s[:ost]
# print(min)
# q = f"{min}-" if min else ""
#
# cur = ""
# for i in range(ost, len(s)):
#     cur += s[i]
#     if len(cur) == k:
#         q += f"{cur}-"
#         cur = ""
# print(q[:-1])


#Sorting кормим детей
g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
g.sort()
s.sort()
count = 0
i = 0
for c in s:
    if c >= g[i]:
        count += 1
        i += 1
    if i == len(g):
        break
# print(count)


#hash - найти мажорное число в массиве
nums = [3, 2, 3]
# print(Counter(nums).most_common(1)[0][0]) #чит команда


#array
candies = [2,3,5,1,3]
extraCandies = 3
# boolean_mas = [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]
# print(boolean_mas)


#string - переворачиваем все гласные буквы в слове
#Строку можно превратить в массив и работать с ним, это легче
# s = "hello"
# vowels = {"a", "e", "i", "u", "o"}
# s = list(s)
# l, r = 0, len(s) - 1
# while l <= r:
#     if not s[l].lower() in vowels:
#         l += 1
#         continue
#     if not s[r].lower() in vowels:
#         r -= 1
#         continue
#     s[l], s[r] = s[r], s[l]
#     l += 1
#     r -= 1
# print("".join(s))


#divmod - прибавляем к числу в двоичной системе число и выводим ответ
# a = "10"
# #b = 11
# b = "11"

# la, lb = len(a), len(b)
# if la > lb:
#     b = "0" * (la - lb) + b
# else:
#     a = "0" * (lb - la) + a
# prev = 0
# new_str = ""
# for i in range(len(a)-1, -1, -1):
#     d1 = int(a[i])
#     d2 = int(b[i])
#     carry, d = divmod(d1 + d2 + carry, 2)
#     new_str += str(d)
# if carry:
#     new_str += str(carry)
# print(new_str[::-1])


#hash - Самый длинный палиндром
# s = "abccccdd"
# s = "bananas"
# s = "ccc"
s = "abcbe"
c = Counter(s)
ans = 0
for i, j in c.items():
    cur = j - (j % 2)
    ans += cur
    c[i] -= cur
# print(dict(c))
# print(ans if not sum(c.values()) else ans + 1)


#string - вернуть длину последнего слова
# s = "a"
# s = s.split(" ")
# while s[-1] == '':
#     s = s[:-1]
# print(s[-1])
s = "Hello World"
word = ""
for i in range(len(s)-1, -1, -1):
    if s[i] == " ":
        if word:
            pass
            # print(len(word))
    else:
        word += s[i]
# print(len(word))


#array - dp Сосчитать максимальную последовательность 1
# nums = [1,0,1,1,0,1]
# tar = [0] + nums + [0]
# max_col = 0
# cur = 0
# for i in range(len(tar)-1):
#     if tar[i + 1] == 1:
#         cur += 1
#     else:
#         if cur > max_col:
#             max_col = cur
#         cur = 0
# print(max_col)
# nums = [1, 0, 1, 1, 0, 1]
# dp = [0] * (len(nums) + 1)
# for i in range(1, len(dp)):
#     if nums[i - 1]:
#         dp[i] = dp[i - 1] + 1
#     else:
#         dp[i] = 0
# print(dp)


#array
#Максимальная общая подпоследовательность
nums = [1,3,5,4,7]
dp = [1] * (len(nums))
for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        dp[i] = dp[i - 1] + 1
# print(dp)


#array - Two Pointers
#Переносим все дубликаты в конец массива и возвращаем индекс последнего уникального эдемента
nums = [0,0,1,1,1,2,2,3,3,4]
j = 0
for i in range(len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[i], nums[j] = nums[j], nums[i]
# print(j, nums)


#Array - prefix sum - к каждому числу массива прибалвляем сумму последующих чисел массива
nums = [1, 2, 3, 4]
prefix_sum = nums[0]
for i in range(1, len(nums)):
    prefix_sum += nums[i]
    nums[i] = prefix_sum
# print(nums)
#Короткая версия
# for i in range(1, len(nums)):
#     nums[i] += nums[i - 1]
# print(nums)


#hash - являются ли числа аморфными
s = "eggg"
t = "aesq"
# s = "foo"
# t = "bar"
d1 = {}
d2 = {}
for i in range(len(s)):
    if s[i] in d1:
        if d1[s[i]] != t[i]:
            # print(False)
            break
    else:
        if t[i] in d2 and d2[t[i]] != s[i]:
            # print(False)
            break
        else:
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]
# print(d1)
# print(d2)
# print(True)


#hash - Найти общие элементы у двух массивов
nums1 = [1,2,2,1]; nums2 = [2,2]
nums1 = set(nums1)
nums2 = set(nums2)
# print(nums1 & nums2)
#Альтернатива с Counter
# cnt1 = Counter(nums1)
# cnt2 = Counter(nums2)
# print(cnt1 & cnt2)


#sliding window (nums[i] == nums[j] and abc(j - i) <= k
nums = [1,0,1,1]
k = 1
hash = dict()
for i in range(len(nums)):
    if nums[i] in hash and i - hash[nums[i]] <= k:
        pass
        # print(1)
    hash[nums[i]] = i


#string - максимальный префикс из массива слов
# strs = ["flower", "flow", "flight"]
# max_prefix = ""
# for i in range(1, len(strs)):
#     k = 0
#     cur_prefix = ""
#     while k < len(strs[i - 1]) and k < len(strs[i]) and strs[i - 1][k] == strs[i][k]:
#         cur_prefix += strs[i][k]
#         k += 1
#     strs[i] = cur_prefix
# print(strs[-1])
# strs = ["flower", "flow", "flight"]
# ans = ""
# for i, l in enumerate(strs[0]):
#     for word in strs[1:]:
#         if i > len(word) - 1 or word[i] != l:
#             pass
#             print(ans)
#     ans += l
# print(ans)


#hash - Two sum
# nums = [2,7,11,15]
# target = 9
# hash = {}
# for i, num in enumerate(nums):
#     comp = target - num
#     if comp in hash:
#         print([i, hash[comp]])
#     hash[num] = i


#stack
str = "(())[]{}"
stack = list()
hash = {
    "(": ")",
    "[": "]",
    "{": "}",
}
for i, j in enumerate(str):
    if j in "([{":
        stack.append(j)
    else:
        if not stack or j != hash[stack.pop()]:

            print("No")
# print(len(stack) == 0)


# math
# Простой способ конвертировать бинарное число в десятичное на ходу
# n = [1, 1, 1, 1]
# ans = 0
# for i in n:
#     ans = ans * 2 + i
# print(ans)
#Плохое решение
# a_mas = [1, 0, 1]
# a = 0
# n = len(a_mas) - 1
# for i in a_mas:
#     a += i * (10 ** n)
#     n -= 1
# print(a)
# a = 101
# b = 0
# sum = 0
# while a:
#     cur = a % 10
#     sum += cur * (2 ** b)
#     b += 1
#     a //= 10
# print(sum)


#bitwice - число битов (едениц)
# n = 11111111111111111111111111111101
# ans = 0
# while n:
#     ans += n & 1
#     n >>= 1
# print(ans)


#Two pointers - убираем все нечетные числа в конец массива
# nums = [3, 1, 2, 4]
# j = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         j += 1


#array - определяем, является ли массив монотонным (возрастает либо же убывает)
# nums = [6,5,4,4]
# ex = nums[0] < nums[-1]
# for i in range(len(nums) - 1):
#     if nums[i] < nums[i + 1]:
#         flag = True
#         if not ex and flag:
#             print(False)
#             exit()
#     elif nums[i] > nums[i + 1]:
#         flag = False
#         if ex and not flag:
#             print(False)
#             exit()
# print(True)
nums = [6,5,4,4]
dec, inc = True, True
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        dec = False
    if nums[i] < nums[i - 1]:
        inc = False
# print(dec or inc)


#Two Pointers - сдвигаем все числа, равные val вправо
nums = [3, 2, 2, 3]
val = 3
j = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
# print(j)


#hash - указываем числа, встречаются в range(1, n) но не вст. в nums
nums = [4,3,2,7,8,2,3,1]
st_nums = set(range(1, len(nums) + 1)) - set(nums)
# print(st_nums)
razn = list(st_nums)
# print(razn)


#string - указываем индекс, с которого начинается подстрока
# haystack = "mississippi"
# needle = "issip"
# rev_index = 0
# j = 0
# gr = len(needle)
# for i in range(len(haystack)):
#     if i + gr > len(haystack):
#         print(-1)
#         exit()
#     for u in range(i, i+gr):
#         # print(haystack[u], end=" ")
#         if haystack[u] == needle[j]:
#             print(j, end=" ")
#             j += 1
#             if j == gr:
#                 print(rev_index)
#                 exit()
#         else:
#             j = 0
#             rev_index += 1
#             break
# haystack = "mississippi"
# needle = "issip"
# lh = len(haystack)
# ln = len(needle)
# for i in range(lh - ln + 1):
#     if haystack[i:i+ln] == needle:
#         print(i)
# print(-1)


#Two Pointers - вернуть массив квадратов чисел
nums = [-4,-1,0,3,10]
l, r = 0, len(nums) - 1
ans = []
while l <= r:
    # print(nums[l], nums[r])
    if abs(nums[r]) > abs(nums[l]):
        ans.append(nums[r] * nums[r])
        r -= 1
    else:
        ans.append(nums[l] * nums[l])
        l += 1
# print(ans[::-1])


#hash
jewels = "aA"
stones = "aAAbbbb"
ans = 0
jewels = set(jewels)
for i in stones:
    if i in jewels:
        ans += 1
# print(ans)


#hash
s = "leetcode"
cnt = Counter(s)
for i, j in enumerate(s):
    if j in cnt and cnt[j] == 1:
        pass
        # print(i)
        # exit()


#hash
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
cnt_r = Counter(ransomNote)
cnt_m = Counter(magazine)
for i in cnt_m:
    if i not in cnt_r:
        continue
    cnt_r[i] -= cnt_m[i]
    if cnt_r[i] <= 0:
        pass
#         print("No")
# print(max(cnt_r.values()) <= 0)
#Более эффективный способ
# print(Counter(ransomNote) & Counter(magazine) == Counter(ransomNote))


#Fibonacci








































































































