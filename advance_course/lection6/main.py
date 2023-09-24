class Stack:
    def __init__(self) -> None:
        self.mas = []
    
    def push(self, x):
        self.mas.append(x)
    
    def pop(self):
        return self.mas.pop()
    def isEmpty(self):
        return len(self.mas) == 0

#Очередь на двух стеках
class Queue:
    def __init__(self, s1: Stack, s2: Stack) -> None:
        self.stack1 = s1
        self.stack2 = s2

    def add(self, x):
        self.stack1.push(x)

    def remove(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()



s1 = Stack()
s2 = Stack()

queue = Queue(s1, s2)
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.remove())
print(queue.remove())
print(queue.remove())

