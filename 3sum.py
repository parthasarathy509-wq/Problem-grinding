def threeSum(nums):
    nums.sort()  # Sort in-place first
    res = []

    for i in range(len(nums) - 2):
        # If the current smallest number is > 0, no three numbers can sum to 0
        if nums[i] > 0:
            break

        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set up two pointers for the remaining part of the array
        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total < 0:
                l += 1  # Sum is too small, move left pointer right
            elif total > 0:
                r -= 1  # Sum is too big, move right pointer left
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # Skip duplicate values for the left and right pointers
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return res


threeSum([-2, 0, 1, 1, 2])
