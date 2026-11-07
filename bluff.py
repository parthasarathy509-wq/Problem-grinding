a = 8
is_prime = True
for i in range(2, int(a**0.5) + 1):
    if a % i == 0:
        is_prime = False
        break
print(is_prime)
