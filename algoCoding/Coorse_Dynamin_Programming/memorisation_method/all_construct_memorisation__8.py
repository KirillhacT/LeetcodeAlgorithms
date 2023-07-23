#O(n ^ m)
#O(m)
def badAllConstruct(target, wordBank):
    if target == "":
        return [[]]
    cur = []
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            res = badAllConstruct(target[cur_len:], wordBank)
            if res:
                res = [[i] + res[j] for j in range(len(res))]
                # for j in range(len(res)):
                #     res[j] = [i] + res[j]
                cur += res
    return cur
# print(badAllConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(badAllConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(badAllConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(badAllConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# t = [[]]
# cur = []
# cur += t
# print(cur)

# c = [[]]
# c[0].append(1)
# c[0].append(2)

# c = [[1, 2]]
# b = [[3, 4]]
# print(c + b)

memo = {}
def goodAllConstruct(target, wordBank):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    cur = []
    for i in wordBank:
        cur_len = len(i)
        if target[:cur_len] == i:
            res = goodAllConstruct(target[cur_len:], wordBank)
            if res:
                res = [[i] + res[j] for j in range(len(res))]
                # for j in range(len(res)):
                #     res[j] = [i] + res[j]
                cur += res
    memo[target] = cur
    return cur
# print(goodAllConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(goodAllConstruct("aaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
