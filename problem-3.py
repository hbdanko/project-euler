from sympy import factorint

def largest_prime_factor(prime):
    return max(factorint(prime))

#print(largest_prime_factor(600851475143))

deneme = factorint(600851475143)
print(largest_prime_factor(600851475143))