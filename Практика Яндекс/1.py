s = "AABBCCCCXYYYYYYSRRRTTTTHGgg"
def pack(s, cnt):
    if cnt != 1:
        return s + str(cnt)
    return s
# stri = []
# count = 1
# for i in range(len(s)):
#     if i + 1 >= len(s):
#         stri.append(pack(s[i], count))
#     elif s[i] == s[i + 1]:
#         count += 1
#     else:
#         stri.append(pack(s[i], count))
#         count = 1
# print("".join(stri))
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







