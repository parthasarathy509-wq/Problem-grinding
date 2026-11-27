def characterReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])

        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# --- Test Cases ---

# 1. Standard LeetCode examples
print("Test 1 ('ABAB', k=2):", characterReplacement("ABAB", 2))        # Expected: 4
print("Test 2 ('AABABBA', k=1):", characterReplacement("AABABBA", 1))  # Expected: 4

# 2. Zero replacements allowed (k = 0)
print("Test 3 ('AAABBC', k=0):", characterReplacement("AAABBC", 0))    # Expected: 3

# 3. Enough replacements to change the entire string
print("Test 4 ('ABCDE', k=4):", characterReplacement("ABCDE", 4))      # Expected: 5
print("Test 5 ('ABCDE', k=10):", characterReplacement("ABCDE", 10))    # Expected: 5

# 4. Single character string
print("Test 6 ('A', k=0):", characterReplacement("A", 0))              # Expected: 1
print("Test 7 ('A', k=2):", characterReplacement("A", 2))              # Expected: 1

# 5. All characters are already identical
print("Test 8 ('ZZZZZ', k=2):", characterReplacement("ZZZZZ", 2))      # Expected: 5

# 6. Empty string edge case
print("Test 9 ('', k=2):", characterReplacement("", 2))                # Expected: 0
