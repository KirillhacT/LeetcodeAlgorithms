#O(n ^ m * m) -> O(n * m ^ 2)
#O(m ^ 2) -> O(m ^ 2)

def badCanConstruct(target, wordBank):
    if target == "":
        return 1
    cur = 0
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            res = badCanConstruct(target[cur_len:], wordBank)
            cur += res
    return cur

# print(badCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(badCanConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(badCanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(badCanConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

memo = {}
def goodCanConstruct(target, wordBank):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    cur = 0
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            res = goodCanConstruct(target[cur_len:], wordBank)
            cur += res
    memo[target] = cur
    return cur

print(goodCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(goodCanConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(goodCanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(goodCanConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
