# x = int(input())
# y = int(input())
#
# mas = [0] * 10
# while x:
#     mas[x % 10] += 1
#     x //= 10
# while y:
#     mas[y % 10] -= 1
#     y //= 10
#
# print(not any(mas))

#Ладьи
def countbeatingrooks(rookcoords):
    def addrock(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1
    def countPairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        print(pairs)
        return pairs
    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        # print(row, col)
        addrock(rooksinrow, row)
        addrock(rooksincol, col)
    return countPairs(rooksinrow) + countPairs(rooksincol)
rookcoords = [(0, 0), (0, 5), (1, 3), (2, 4), (3, 1), (3, 4), (4, 2), (5, 0), (5, 5)]
# print(countbeatingrooks(rookcoords))
#Ферзи
def countbeatingqueens(queencoords):
    def addqueen(diags, row, col):
        if col - row not in diags:
            diags[col - row] = 0
        if col + row not in diags:
            diags[col + row] = 0
        diags[col - row] += 1
        diags[col + row] += 1
    def countPairs(diags):
        pairs = 0
        for key in diags:
            pairs += ((diags[key] - 1) * diags[key]) // 2
        return pairs

    queenindiags1 = {}
    queenindiags2 = {}
    for row, col in queencoords:
        addqueen(queenindiags1, row, col)
        addqueen(queenindiags2, row, col)

    return countPairs(queenindiags1) + countPairs(queenindiags2)

#Гистограмма
# s = "Hello world!"
# symcount = {}
# maxsumcount = 0
# for symbol in s:
#     if symbol not in symcount:
#         symcount[symbol] = 0
#     symcount[symbol] += 1
#     maxsumcount = max(maxsumcount, symcount[symbol])
# # print(symcount, maxsumcount)
# sorteduniquesyms = sorted(symcount.keys())
# print(sorteduniquesyms)
# for row in range(maxsumcount, 0, -1): #От 3 -> 0
#     for sym in sorteduniquesyms: #Ключи -> [' ', '!', 'H', 'd', 'e', 'l', 'o', 'r', 'w']
#         if symcount[sym] >= row:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
# print("".join(sorteduniquesyms))

# def keybyword(word):
#     return "".join(sorted(word))
def keybyword(word):
    symcnt = {}
    for sym in word:
        if sym not in symcnt:
            symcnt[sym] = 0
        symcnt[sym] += 1
    lst = []
    for sym in sorted(symcnt.keys()):
        lst.append(sym)
        lst.append(str(symcnt[sym]))
    print(lst)
    return "".join(lst)

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
b = {}
for word in a:
    cur = keybyword(word)
    if cur not in b:
        b[cur] = []
    b[cur].append(word)
# print(b)
ans = []
for word in b.values():
    ans.append(word)
print(ans)





