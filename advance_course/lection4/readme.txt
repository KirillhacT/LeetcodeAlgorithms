Не существует сортировок, сравнивающие элементы и работающие менее чем 
за O(logN)

пусть нам дан a[0..n-1]
где a[i] принадлежит [0..m-1]
где m маленькое
m = 3
a = [2, 0, 1, 2, 1, 1, 0, 2, 1]
cnt [0, 0, 0] --> [2, 4, 3]
a2 = 0, 0, 1, 1, 1, 1, 2, 2, 2 -> O(n + m)

Но если в массиве будут лежать объекты, у которых есть ключ, по которому мы сортируем
class Item {
    int key; //[0..m-1]
    Data data;
}   
a = [A:2, B:0, B:1, C:2, D:1, F:1, G:0, H:2, I:1]
cnt [0, 0, 0] --> [2, 4, 3]
заведем массив длиной 2 + 4 + 3

     e,e,,,e,, //e -> место для первого элемента из массива подсчета
a = [.........]
     001111222 //места для 0, 1, 2

Такой подход эффективен, если m маленькое 
Но если мы имеем, что a[i] принадлежит [0..m^2-1]
Создавать массив размера m^2 дорого поэтому:
возьмем x = [0..m^2-1]
x = a * m + b, где a, b принадлежат [0..m-1]
m = 10 -> [0..99]
x = a * 10 + b

a[i] = b[i] * m + c[i]
отсортировать a[i] это тоже самое, что и отсортировать пары (b[i], c[i])
Сортировкой пар занимается цифровая сортировка

пусть у нас есть пары:
a = [02, 21, 01, 11, 21, 20, 02, 00]
наивное решение:
создать массив и разбить его на блоки, начинающиеся с 0, 1, 2 и потом их отдельно 
отсортировать
[0x.....1x.......2x......]
    n0      n1      n2
  n0 + m  n1 + m  n2 + m
более эффективное:
подсчитать элементы по второй цифре
при a = [02, 21, 01, 11, 21, 20, 02, 00]
cnt = [2, 4, 2]
       0  1  2
a2 = [20, 00, 21, 01, 11, 21, 02, 02]
      0...........1...........2.....
затем подсчитываем элементы в массиве по 1 цифрк
cnt = [4, 1, 3]
a3 = [00, 01, 02, 02, 11, 20, 21, 21]
      0...............1.......2.....
массив пар отсортирован

если a[i] принадлежат O(0..m^k-1)
O(k * (n + m))

Сортирующие сети
у нас есть функция компаратор
cmp(i, j):
    if a[i] > a[j]:
        swap(a[i], a[j])
n = 2
    cmp(0, 1)
n = 3
    cmp(0, 1)
    cmp(0, 2)
    cmp(1, 2)

Сортирующая сеть 3 элементов
a[0] -.---.-------
      |   |
a[1] -.---|---.---
          |   |
a[2] -----.---.---

Bitonic sort
a = [0, 0, 1, 1, | 1, 1, 1, 0] делим массив на половину 
a2 = [0, 0, 1, 0][1, 1, 1, 1] -> оба массива становятся бетонной последовательностью 



