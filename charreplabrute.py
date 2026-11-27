def characterReplacementPureLogic(s: str, k: int) -> int:
    max_length = 0
    unique_letters = set(s)  # Just like your original idea!

    # Try making a streak out of each unique letter one by one
    for target in unique_letters:
        # Try starting our streak from every possible index in the string
        for start in range(len(s)):
            changes_used = 0
            current_streak = 0

            # Walk forward from 'start' and literally simulate replacing characters
            for i in range(start, len(s)):
                if s[i] == target:
                    # Already matches! Keep going
                    current_streak += 1
                elif changes_used < k:
                    # Doesn't match, so spend 1 change to turn it into 'target'
                    changes_used += 1
                    current_streak += 1
                else:
                    # Out of changes and hit a different letter—streak breaks!
                    break

            max_length = max(max_length, current_streak)

    return max_length


# --- Test ---
print(characterReplacementPureLogic("AABABBA", 1))  # Output: 4
print(characterReplacementPureLogic("ABAB", 2))  # Output: 4
