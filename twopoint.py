a = [1, 2, 3, 4, 5]
l = 0
r = len(a) - 1
while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
print(a)
