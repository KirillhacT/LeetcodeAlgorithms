#1
# D = int(input())
# E = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
#
# def sortr(first, second):
#     if first > second:
#         return (first, second)
#     return (second, first)
#
#
# a, b = sortr(a, b)
# b, c = sortr(b, c)
# a, b = sortr(a, b)
# D, E = sortr(D, E)
# print(a <= D and b <= E)

#2
n = int(input())
m = int(input())
a = int(input())
b = int(input())

#(n - 1) * (a + 1) + 1
#¬ первом варианте интервал равен a, в другом b
minT1 = (n - 1) * a + n #ƒобавл€етс€ как врем€ ожидани€ каждого поезда
maxT1 = (n - 1) * (a + 1) + 1 + (2 * a)
minT2 = (m - 1) * (b + 1) + 1
maxT2 = (m - 1) * (b + 1) + 1 + (2 * b)

minans = max(minT1, minT2)
maxans = min(maxT1, maxT2)
if not maxans < minans:
    print(minans, maxans)



