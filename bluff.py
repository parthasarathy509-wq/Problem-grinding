def topKFrequent(nums, k):
    a = {}
    b = []
    res = []
    fin = []
    for i in range(len(nums)):
        count = 1
        if nums[i] in a:
            count = a[nums[i]]
            count += 1
        a[nums[i]] = count
    for i, j in a.items():
        b.append(j)
    b.sort(reverse=True)
    for i in range(k):
        res.append(b[i])
    for i in res:
        for key, value in a.items():
            if i == value:
                fin.append(key)
                a[key] = -1
                break
    return fin


print(topKFrequent([7, 7], 1))
