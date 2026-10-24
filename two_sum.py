def twoSum(nums, target: int):
    a = {}
    r = []
    for i, n in enumerate(nums):
        miss = target - n
        if miss in a:
            r.append([a[miss], i])
        a[n] = i
    return r


print(twoSum([6, 1, 5, 2, 3, 4], 7))
