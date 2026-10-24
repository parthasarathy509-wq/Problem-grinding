def twoSum(nums, target: int):
    a = {}
    for i, n in enumerate(nums):
        miss = target - n
        if miss in a:
            return a[miss], i
        a[n] = i


print(twoSum([3, 4, 5, 6], 7))
