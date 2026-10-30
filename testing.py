while True:
    a = int(input("enter or enter -1 to end:"))
    if a == -1:
        break
    b = int(input("enter end:"))
    if a <= 1:
        a = 2
    while a <= b:
        is_prime = True

        i = 2
        while i < int(a**0.5) + 1:
            if a % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(a)
        a += 1
