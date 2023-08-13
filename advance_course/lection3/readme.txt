Быстрая Сортировка - рандомизированный алгоритм (Implace)

a = [....l,,,,,r...]

sort(l, r)
    x = a[random(l, r-1)]
    if r - l == 1
        return
    m = l
    for i = l...r-1
        if a[i] < x:
            swap(a[i], a[m])
            m++
    sort(l, m)
    sort(m, r)

К-я порядковая статистика
Алгоритм Хоара
Выбираем рандомное число
Делим по этому числу на два массива
Выкидываем кусок массива, где элемента c индексом k нету и рекурсивно
повторяем

a = [l...............r]
find(l, r, k)
    x = a[random(l, r-1)]
    if r - l == 1
        return a[k]
    m = l
    for i = l...r-1
        if a[i] < x:
            swap(a[i], a[m])
            m++
    if k < m:
        find(l, m, k)
    else:
        find(m, r, k)


