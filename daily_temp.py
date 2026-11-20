def dailyTemperatures(temperatures):
    res = []
    n = len(temperatures)
    t = temperatures
    for i in range(n):
        if i == n - 1:
            res.append(0)
        for j in range(i + 1, n):
            if t[i] < t[j]:
                res.append(j - i)
                break
            if j == n - 1:
                res.append(0)
    return res


print(dailyTemperatures([90, 80, 70, 60, 50]))  # Expected: [0, 0, 0, 0, 0]
print(dailyTemperatures([70, 70, 70, 70]))  # Expected: [0, 0, 0, 0]
print(dailyTemperatures([70, 70, 70, 75]))  # Expected: [3, 2, 1, 0]
print(dailyTemperatures([55]))  # Expected: [0]
print(dailyTemperatures([80, 40, 35, 30, 85]))  # Expected: [4, 3, 2, 1, 0]
