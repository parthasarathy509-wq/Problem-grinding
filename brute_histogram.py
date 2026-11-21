def largestRectangleArea(heights):
    n = len(heights)
    if n == 0:
        return 0
    areas = []

    for i in range(n):
        h = heights[i]

        # 1. Stretch left while bars are >= h
        left = i
        while left > 0 and heights[left - 1] >= h:
            left -= 1

        # 2. Stretch right while bars are >= h
        right = i
        while right < n - 1 and heights[right + 1] >= h:
            right += 1

        # 3. Width is from left to right inclusive
        width = right - left + 1
        areas.append(h * width)

    return max(areas)


# --- Edge Case & Standard Test Cases ---

# 1. LeetCode Standard Example 1 (Expected: 10)
print("Test 1 (Standard):", largestRectangleArea([2, 1, 5, 6, 2, 3]))

# 2. LeetCode Standard Example 2 (Expected: 4)
print("Test 2 (Two bars):", largestRectangleArea([2, 4]))

# 3. Single Bar (Expected: 5)
print("Test 3 (Single element):", largestRectangleArea([5]))

# 4. Empty List (Expected: 0)
print("Test 4 (Empty):", largestRectangleArea([]))

# 5. All Zeros (Expected: 0)
print("Test 5 (All zeros):", largestRectangleArea([0, 0, 0]))

# 6. Zero in the Middle - Splits the histogram (Expected: 4)
print("Test 6 (Zero gap):", largestRectangleArea([2, 3, 0, 4]))

# 7. All Equal Heights (Expected: 12 -> 3 * 4)
print("Test 7 (All equal):", largestRectangleArea([3, 3, 3, 3]))

# 8. Strictly Increasing Heights (Expected: 9 -> height 3 * width 3)
print("Test 8 (Increasing):", largestRectangleArea([1, 2, 3, 4, 5]))

# 9. Strictly Decreasing Heights (Expected: 9 -> height 3 * width 3)
print("Test 9 (Decreasing):", largestRectangleArea([5, 4, 3, 2, 1]))

# 10. Valley Shape - Dip in the middle (Expected: 6 -> height 1 * width 6)
print("Test 10 (Valley):", largestRectangleArea([4, 2, 1, 1, 2, 4]))

# 11. Peak Shape - Tallest in the middle (Expected: 8 -> height 2 * width 4)
print("Test 11 (Peak):", largestRectangleArea([1, 2, 5, 2, 1]))
