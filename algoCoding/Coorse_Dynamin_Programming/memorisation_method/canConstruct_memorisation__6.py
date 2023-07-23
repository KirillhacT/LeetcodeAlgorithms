#O(n ^ m * m) -> O(n * m ^ 2)
#O(m ^ 2) -> 0(m ^ 2)
def badCanConstruct(target, wordBank):
    if target == "":
        return True
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            if badCanConstruct(target[cur_len:], wordBank):
                return True
    return False
# print(badCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(badCanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(badCanConstruct("enterapotentpot", ["a", "po", "ent", "enter", "ot", "o", "t"]))
# a = "abcdef"
# c = "abc"
# print(a[:len(c)])

memo = {}
def goodCanConstruct(target, wordBank):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            if goodCanConstruct(target[cur_len:], wordBank):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(goodCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(goodCanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(goodCanConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))