def isAnagram(s: str, t: str) -> bool:
    a = {}
    b = {}
    for i in s:
        count = 1
        if i in a:
            count = a[i]
            count += 1
        a[i] = count
    for j in t:
        count = 1
        if j in b:
            count = b[j]
            count += 1
        b[j] = count
    if a == b:
        return True
    else:
        return False


# --- TEST CASES FOR VS CODE ---
test_cases = [
    # Format: (string_s, string_t, expected_outcome)
    ("anagram", "nagaram", True),  # Standard matching anagram
    ("rat", "car", False),  # Same length, completely different letters
    ("hello", "hell", False),  # Different lengths
    ("a", "ab", False),  # One string is a subset of the other
    ("ab", "ba", True),  # Short matching anagram
    (
        "Awesome",
        "awesome",
        False,
    ),  # Case-sensitivity check (Capital 'A' vs lowercase 'a')
]

print("--- Running Anagram Tests ---")
for idx, (s, t, expected) in enumerate(test_cases, 1):
    result = isAnagram(s, t)
    status = "✅ PASSED" if result == expected else "❌ FAILED"
    print(
        f"Test {idx}: s='{s}', t='{t}' -> Got: {result} | Expected: {expected} [{status}]"
    )
