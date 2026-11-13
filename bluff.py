def longestConsecutive(nums):
    num = sorted(nums)
    s = set(num)
    k = list(s)
    l = 0
    r = 1
    count = 1
    max_count = 1
    while r < len(k):
        if k[l] == (k[r] - 1):
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
        l += 1
        r += 1
    return max_count


print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
