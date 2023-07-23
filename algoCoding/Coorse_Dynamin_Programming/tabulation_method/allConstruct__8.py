#O(m ^ 2 * n)
#O(m)
def allConstruct(target, wordList):
    mas = [[] for _ in range(len(target) + 1)]
    mas[0] = [[]]
    for i in range(len(target) + 1):
        if mas[i] != []:
            #TODO!
            for word in wordList:
                pass
                #Если слово соответсвует символам начиная с
                #позиции i
                # if target[i:i+len(word)] == word:
                #     new_mas = [for i in range(word)]

    return mas

# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

# target = "длъ"
# mas = [[] for _ in range(len(target) + 1)]
# mas[0] = [[]]
# print(mas)