class Heap:
    def __init__(self) -> None:
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        #Пока i не корень и пока родитель больше ребенка, меняем
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2
    
    def remove_min(self):
        res = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        n = len(self.heap)

        i = 0
        #i -> элемент который меняем (текущий)
        #j -> наименьший из дочерних элементов (с которым меняем)
        while True:
            j = i
            if (2 * i) + 1 < n and self.heap[j] > self.heap[(2 * i) + 1]:
                j = (2 * i) + 1
            if (2 * i) + 2 < n and self.heap[j] > self.heap[(2 * i) + 2]:
                j = (2 * i) + 2
            if i == j:
                break
            self.swap(i, j)
            i = j
        return res
    def __str__(self) -> str:
        print(self.heap)

# heap = Heap()
# mas = [3, 1, 6, 2, 5, 9, 2]

# for i in range(len(mas)):
#     heap.insert(mas[i])
# for i in range(len(mas)):
#     mas[i] = heap.remove_min()
# print(mas)



#Implace вариант
heap = [3, 1, 6, 2, 5, 9, 2] 


def swap(i, j):
        heap[i], heap[j] = heap[j], heap[i]

#Чтобы сортировка кучей была корректна она должна хранить элементы по убыванию (от большего к меньшему)
def sift_up(i):
    while i > 0 and heap[i] > heap[(i - 1) // 2]: 
        swap(i, (i - 1) // 2)
        i = (i - 1) // 2

def sift_down(i, n):
        i = 0
        while True:
            j = i
            if (2 * i) + 1 < n and heap[j] < heap[(2 * i) + 1]:
                j = (2 * i) + 1
            if (2 * i) + 2 < n and heap[j] < heap[(2 * i) + 2]:
                j = (2 * i) + 2
            if i == j:
                break
            swap(i, j)
            i = j

#Более быстрый но сложный вариант первого цикла
# for i in range(len(heap)-1, -1, -1): # --> O(n)
#     sift_down(i, len(heap))

for i in range(len(heap)):  #--> O(nlogn)
    sift_up(i)
for i in range(len(heap)-1, -1, -1): # n - 1 -> 0:
    swap(0, i)
    sift_down(0, i)
print(heap)







    




