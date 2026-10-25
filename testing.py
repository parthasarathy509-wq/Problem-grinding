def isAnagram(s: str, t: str) -> bool:
    a = {}
    b = {}
    for i, n in enumerate(s):
        count = 1
        if n in a:
            count += a[n]
            a[n] = count
        a[n] = count
    for j, m in enumerate(t):
        count = 1
        if m in b:
            count += b[m]
            b[m] = count
        b[m] = count
    return a == b


print(isAnagram("racecar", "carrace"))
