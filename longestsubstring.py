def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    r = 0
    maxi = 0
    se = {}
    while r < len(s):
        while s[r] in se:
            se.pop(s[l])
            l += 1
        se[s[r]] = r
        maxi = max(maxi, r - l + 1)
        r += 1
    return maxi


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
