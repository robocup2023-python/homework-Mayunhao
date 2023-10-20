primes = []

for num in range(101, 201):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print("101-200之间的所有素数:")
for prime in primes:
    print(prime)
