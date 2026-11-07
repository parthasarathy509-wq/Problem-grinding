def two(nums, target):
    a = {}
    for i, n in enumerate(nums):
        miss = target - n
        if miss in a:
            return [a[miss], i]
        a[n] = i


print(two([2, 7, 11, 15], 9))
