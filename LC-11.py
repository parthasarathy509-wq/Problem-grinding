def maxArea(height: list[int]) -> int:
    a = []
    for i, n in enumerate(height, start=1):
        for j, e in enumerate(height, start=1):
            if i == j:
                continue
            if n < e:
                l = n * (j - i)
                a.append(l)
            if n > e:
                M = e * (j - i)
                a.append(M)

    return max(a)


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
