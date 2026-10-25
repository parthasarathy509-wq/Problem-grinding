def fact(a):
    if a < 0:
        raise ValueError("Invalid number")
    if a <= 1:
        return 1
    b = fact(a - 1) * a
    return b


m = int(input("enter:"))
l = fact(m)
print(l)
