def trap(height):
    if not height:
        return 0
    n = len(height)
    res = 0

    for i in range(n):
        leftMax = height[i]
        rightMax = height[i]

        for j in range(i):
            leftMax = max(leftMax, height[j])

        for j in range(i + 1, n):
            rightMax = max(rightMax, height[j])

        res += min(leftMax, rightMax) - height[i]
    return res


print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
