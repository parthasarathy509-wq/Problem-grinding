class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Take the first word as our reference base
        base = strs[0]

        # Loop through each character index of the base word
        for i in range(len(base)):
            char = base[i]

            # Check this same index 'i' in all other words
            for other_word in strs[1:]:
                # Check if we ran out of letters in the other word,
                # or if the characters don't match
                if i == len(other_word) or other_word[i] != char:
                    # Return everything up to this index
                    return base[:i]

        return base


# --- HOW TO CALL THE FUNCTION ---

# 1. Create an instance of the Solution class
solver = Solution()

# 2. Define your test list of strings
test_words = ["flower", "flow", "flight"]

# 3. Call the function using the instance and store the result
result = solver.longestCommonPrefix(test_words)

# 4. Print the final output to the console
print(f"The longest common prefix is: '{result}'")
