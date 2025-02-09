from sympy import isprime

def prime_generator():
    num = 3
    while True:
        if isprime(num):
            yield num

        if num + 2 != 5 and str(num + 2).endswith('5'):
            num += 4
        else:
            num += 2

def nth_prime(n):
    if n == 1:
        return 2
    else:
        gen = prime_generator()
        count = 1
        prime = 2

        while count != n:
            prime = next(gen)
            count += 1

    return prime

print(nth_prime(10_001))