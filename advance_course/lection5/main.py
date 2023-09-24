mas = [2, 5, 8, 12, 21, 27, 35]
x = 27
# l, r = 0, len(mas)-1
# while l <= r:
#     m = (l + r) // 2
#     val = mas[m]
#     if val == x:
#         print(m)
#         break
#     elif val > x:
#         r = m - 1
#     else:
#         l = m + 1

#Ищем минимальное число, которое либо равно х либо немного больше его
x = 24
l, r = -1, len(mas) #!
while r - l > 1:
    m = (l + r) // 2
    if mas[m] < x:
        l = m
    else:
        r = m
# print(mas[r])

#Ищем минимальное число, которое либо равно х либо немного меньше его
x = 9
l, r = -1, len(mas) #!
while r - l > 1:
    m = (l + r) // 2
    if mas[m] <= x:
        l = m
    else:
        r = m
# print(mas[l])


def good(x):
    return (x // n) * (x // m) >= n

#Бинарный поиск по ответу
w, h, n = 2, 2, 10
l = 0
r = max(w, h) * n #max(w, h) * n^0,5
while r - l > 1:
    m = (l + r) // 2
    if good(m):
        r = m
    else:
        l = m
# print(r)

#Троичный поиск
# def ternary_search(arr, left, right, target):
#     if right >= left:
#         mid1 = left + (right - left) // 3
#         mid2 = right - (right - left) // 3

#         if arr[mid1] == target:
#             return mid1
#         if arr[mid2] == target:
#             return mid2

#         if target < arr[mid1]:
#             return ternary_search(arr, left, mid1 - 1, target)
#         elif target > arr[mid2]:
#             return ternary_search(arr, mid2 + 1, right, target)
#         else:
#             return ternary_search(arr, mid1 + 1, mid2 - 1, target)

#     return -1

# # Пример использования
# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# target = 12

# result = ternary_search(arr, 0, len(arr) - 1, target)

# if result != -1:
#     print("Элемент найден в позиции", result)
# else:
#     print("Элемент не найден")
l = 0
r = 1000
def f(x):
    """Функция растет от 0 до 500, от 500 до +inf она убывает"""
    if x >= 0 and x < 500: 
        return x * 10
    else:
        return x * -10

m1 = (2 * l + r) // 3 
m2 = (l + 2 * r) // 3

# val1, val2 = f(m1), f(m2)
# print(val1, val2)
    
    









