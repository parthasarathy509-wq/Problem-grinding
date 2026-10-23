def isAnagram(s: str, t: str) -> bool:
    a = {}
    b = {}

    for i in s:
        count = 1
        if i in a:
            count = a[i]
            count += 1
        a[i] = count

    for j in t:
        count = 1
        if j in b:
            count = b[j]
            count += 1
        b[j] = count

    return a == b


s = isAnagram("anagram", "nagaram")
print(s)
