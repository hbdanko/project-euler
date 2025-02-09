from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(ceiling):
    multiple = 1
    for num in range(2, ceiling + 1):
        multiple = lcm(multiple, num)
    return multiple

print(smallest_multiple(20))