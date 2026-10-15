class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        base = strs[0]
        for i in range(len(base)):
            char = base[i]

            for other_word in strs[1:]:
                if i == len(other_word) or other_word[i] != char:
                    return base[:i]

        return base


solver = Solution()
test_words = ["flower", "flow", "flight"]
result = solver.longestCommonPrefix(test_words)
print(f"The longest common prefix is: '{result}'")
