def triangular_number_generator():
    index, number = 1, 1

    while True:
        yield number
        index += 1
        number = sum(range(index + 1))

def divisor_count(num):
    count = 0

    for div in range(1, int(num ** (1 / 2)) + 1):
        if num % div == 0:
            count += 1 if div == num // div  else 2

    return count

def divisible_triangular_number(div_count):
    max_divisible = 0
    gen = triangular_number_generator()

    while max_divisible <= div_count:
        number = next(gen)
        if divisor_count(number) > max_divisible:
            max_divisible = divisor_count(number)

    return number

print(divisible_triangular_number(500))