#O(m ^ 2 * n)
#O(m)
def countConstruct(target, wordList):
    mas = [0] * (len(target) + 1)
    mas[0] = 1
    for i in range(len(target) + 1):
        if mas[i] != 0:
            for word in wordList:
                #Если слово соответсвует символам начиная с
                #позиции i
                if target[i:i+len(word)] == word:
                    mas[i + len(word)] += mas[i]
    return mas[len(target)]

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))