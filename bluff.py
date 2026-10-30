a = 0
b = 1
n = 11
count = 0
while count < n:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
    count += 1
