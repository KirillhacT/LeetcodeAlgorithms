def maxVowels(self, s: str, k: int) -> int:
    vowel_letters = {'a', 'e', 'i', 'o', 'u'}
    curr = 0
    for i in range( ):
        if s[i] in vowel_letters:
            curr += 1
    ans = curr
    for right in range(k, len(s)):
        if s[right] in vowel_letters:
            curr += 1
        if s[right - k] in vowel_letters:
            curr -= 1
        ans = max(ans, curr)
    return ans