class Union:
    def __init__(self, val) -> None:
        self.val = val
        self.size = 0
        self.next = None
    
    # @classmethod
    # def get(cls, x):
    #     while x and x.next:
    #         x = x.next
    #     return x
    @classmethod
    def get(cls, x):
        if x.next == None:
            print(x)
            return x
        root = cls.get(x.next)
        x.next = root
        return root

    @classmethod
    def union(cls, x, y):
        x = cls.get(x) #3
        y = cls.get(y) #4
        if x.size < y.size:
            x, y = y, x
        y.next = x
        if y.size == x.size:
            x.size += 1
        # if x.size < y.size:
        #     x, y = y, x
        # y.next = x
        # x.size = max(1, x.size + y.size) 
    def __str__(self) -> str:
        return f"{self.val}:{self.size}"
      
        

a1 = Union(1)
a2 = Union(2)
a3 = Union(3)
a4 = Union(4)
a5 = Union(5)
a6 = Union(6)

# Union.union(a1, a2)
# #a2 -> a1
# Union.union(a3, a4)
# #a4 -> a3
# Union.union(a5, a6)
# #a6 -> a5

# Union.union(a1, a4)
# #a4 -> a3 -> a1 <- a2
# Union.union(a2, a6)
# #a4 -> a3 -> a1 <- a2
#            /^\
#             |
#             a5 <- a6
# print(a4, a4.next, a4.next.next)
# print(a6, a6.next, a6.next.next)
 
class LN:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val}"
    @classmethod
    def sjatie(cls, x):
        if x.next == None:
            return x
        root = cls.sjatie(x.next)
        x.next = root
        return root

node1 = LN(1)
node2 = LN(2)
node3 = LN(3)
node4 = LN(4)
node5 = LN(5)
node6 = LN(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

LN.sjatie(node1)
print(node1.next, node2.next, node3.next, node4.next, node5.next)




