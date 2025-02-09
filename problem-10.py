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

def summation_of_primes(ceiling):
    total = 2
    gen = prime_generator()
    
    prime = next(gen)
    while prime < ceiling:
        total += prime
        prime = next(gen)
    
    return total

print(summation_of_primes(10))