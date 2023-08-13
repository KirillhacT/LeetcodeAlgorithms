import random


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


def quicksort(arr, l, r):
    if r - l <= 1:
        print(f"l = {l}, r = {r} --> RETURN...")
        return
    
    pivot = arr[random.randint(l, r-1)]
    middle = l
    print(f"pivot is {pivot}, l = {l}, r = {r}, middle = {middle}")
    print(arr[l:], sep='\t')
    for i in range(l, r):
        if arr[i] < pivot:
            print(f"swap {arr[i]}, {arr[middle]}")
            arr[i], arr[middle] = arr[middle], arr[i]
            middle += 1
    print(arr[l:])
    
    quicksort(arr, l, middle)
    quicksort(arr, middle, r)

# Пример использования
arr = [4, 1, 3, 2, 6, 5]
quicksort(arr, 0, len(arr))
print(arr)

def find(arr, l, r, k):
    if r - l <= 1:
        return arr[k]
    x = arr[random.randint(l, r - 1)]
    m = l

    for i in range(l, r):
        if arr[i] < x:
            swap(arr, i, m)
            m += 1
    if k < m:
        return find(arr, l, m, k)
    else:
        return find(arr, m, r, k)
# arr = [4, 1, 2, 3, 6, 7]
# print(find(arr, 0, len(arr), 2))


            
