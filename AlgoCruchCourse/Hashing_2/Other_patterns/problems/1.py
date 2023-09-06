#Ransom Note
# ransomNote = "a"
# magazine = "aab"
# hash = {}
# for i in magazine:
#     if i not in hash:
#         hash[i] = 0
#     hash[i] += 1
# for j in range(len(ransomNote)):
#     if ransomNote[j] not in hash:
#         print(False)
#         break
#     hash[ransomNote[j]] -= 1
# for key in hash:
#     if hash[key] > 0:
#         print(False)
#         break
# print(True)

#Longest Substring without repeating characters
s = "abcabcbb"
m = -1
hash = set()
l = 0
for r in range(len(s)):
    while s[r] in hash:
        hash.remove(s[l])
        l += 1
    hash.add(s[r])
    m = max(m, r - l + 1)
print(m)




    


