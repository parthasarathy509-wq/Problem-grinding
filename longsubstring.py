def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    st = []
    max_len = 0

    for char in s:
        if char in st:
            max_len = max(max_len, len(st))
            while char in st:
                st.pop(0)
        st.append(char)

    return max(max_len, len(st))


print(lengthOfLongestSubstring(""))  # 0 (empty string)
print(lengthOfLongestSubstring(" "))  # 1 (single space)
print(lengthOfLongestSubstring("a"))  # 1 (single character)
print(lengthOfLongestSubstring("au"))  # 2 (no duplicates at all)
print(lengthOfLongestSubstring("bbbbb"))  # 1 (all identical)
print(lengthOfLongestSubstring("abcabcbb"))  # 3 (standard repeating)
print(lengthOfLongestSubstring("pwwkew"))  # 3 (subsequence trap)
print(lengthOfLongestSubstring("dvdf"))  # 3 (overlapping substring)
print(lengthOfLongestSubstring("anviaj"))  # 5 (duplicate at start + long tail)
print(lengthOfLongestSubstring("abba"))  # 2 (palindrome trap)
print(lengthOfLongestSubstring("tmmzuxt"))  # 5 (stale duplicate before window)
print(lengthOfLongestSubstring("a1! b2@ c3#"))  # 11 (spaces, digits, symbols)
