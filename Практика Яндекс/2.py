class Set:
    def __init__(self, size):
        self.size = size
        self.myset = [[] for i in range(size)]

    def get_hash(self, x):
        return x % self.size

    def add(self, x):
        self.myset[self.get_hash(x)].append(x)

    def find(self, x):
        for now in self.myset[self.get_hash(x)]:
            if now == x:
                return True
        return False

    def delete(self, x):
        xlist = self.myset[self.get_hash(x)]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i], xlist[-1] = xlist[-1], xlist[i]
                xlist.pop()
                return
# from random import randint
# s = Set(10)
# for _ in range(10):
#     rnd = randint(1, 255)
#     print(rnd)
#     s.add(rnd)
# print(s.myset)

#1
# N = int(input())
# X = int(input())
# hash = set()
# for i in range(1, N):
#     if X - i in hash:
#         print(i, X - i)
#         exit()
#     hash.add(i)

#2
# dictionary = []
# text = ""
# goodwords = set(dictionary)
# for word in dictionary:
#     for delpos in range(len(word)):
#         goodwords.add(word[:delpos] + word[delpos+1:])
# ans = []
# for word in text:
#     ans.append(word in goodwords)
# print(ans)





