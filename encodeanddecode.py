def encode(s):
    a = []
    for i in s:
        a.append(str(len(i)) + "#" + i)
    return "".join(a)


s = encode(["hello", "worldi"])


def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        start = j + 1
        end = start + length
        res.append(s[start:end])
        i = end
    return res


print(decode(s))
