h = "hey"


def fact(a):
    n = 1
    for i in range(a):
        n = (i + 1) * n
    return n


print(h, fact(5))
