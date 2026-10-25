def fact(a):
    if a < 0:
        raise ValueError("Invalid number")
    if a <= 1:
        return 1
    return fact(a - 1) * a


print(fact(2))
