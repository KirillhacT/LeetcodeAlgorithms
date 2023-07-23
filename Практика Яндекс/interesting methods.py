#1
#Линейные анализ последовательности
s = "AABBCCCCXYYYYYYSRRRTTTTHGgg"
def pack(s, cnt):
    if cnt != 1:
        return s + str(cnt)
    return s
lastSymbol = s[0]
lasPost = 0
ans = []
for i in range(len(s)):
    if s[i] != lastSymbol:
        ans.append(pack(lastSymbol, i - lasPost)) #!
        lastSymbol = s[i]
        lasPost = i
ans.append(pack(s[lasPost], len(s) - lasPost)) #!
print("".join(ans))


#2
#Гистограмма
s = "Hello world!"
symcount = {}
maxsumcount = 0
for symbol in s:
    if symbol not in symcount:
        symcount[symbol] = 0
    symcount[symbol] += 1
    maxsumcount = max(maxsumcount, symcount[symbol])
# print(symcount, maxsumcount)
sorteduniquesyms = sorted(symcount.keys())
print(sorteduniquesyms)
for row in range(maxsumcount, 0, -1): #От 3 -> 0
    for sym in sorteduniquesyms: #Ключи -> [' ', '!', 'H', 'd', 'e', 'l', 'o', 'r', 'w']
        if symcount[sym] >= row:
            print("#", end="")
        else:
            print(" ", end="")
    print()
print("".join(sorteduniquesyms))