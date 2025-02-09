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
    total = 2  # Start the sum with 2 (the first prime number)
    gen = prime_generator()
    
    prime = next(gen)  # Get the first prime
    while prime < ceiling:
        total += prime
        prime = next(gen)  # Get the next prime
    
    return total

print(summation_of_primes(10))
