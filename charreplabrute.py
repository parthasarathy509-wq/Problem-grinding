def characterReplacementBruteForce(s: str, k: int) -> int:
    max_length = 0
    n = len(s)

    # Outer loop: pick the starting index of the substring
    for i in range(n):
        count = {}  # Fresh frequency map for each new starting index
        max_freq = 0

        # Inner loop: expand the ending index one character at a time
        for j in range(i, n):
            char = s[j]
            count[char] = count.get(char, 0) + 1

            # Find the most frequent character in the current substring s[i...j]
            max_freq = max(max_freq, count[char])

            # Calculate current substring length and required replacements
            substring_len = j - i + 1
            replacements_needed = substring_len - max_freq

            # If valid, update our longest found length
            if replacements_needed <= k:
                max_length = max(max_length, substring_len)

    return max_length


# --- Quick Test ---
print(characterReplacementBruteForce("AABABBA", 1))  # Output: 4
print(characterReplacementBruteForce("ABAB", 2))  # Output: 4
