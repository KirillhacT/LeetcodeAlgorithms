#O(m ^ 2 * n)
#O(m)
def canConstruct(target, wordList):
    mas = [False] * (len(target) + 1)
    mas[0] = True
    for i in range(len(target) + 1):
        if mas[i]:
            for word in wordList:
                #Если слово соответсвует символам начиная с
                #позиции i
                if target[i:i+len(word)] == word:
                    mas[i + len(word)] = True
    return mas[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
