def multiples_of_3_and_5(ceiling):
    return sum([num for num in range(ceiling) if num % 3 == 0 or num % 5 == 0])

print(multiples_of_3_and_5(1000))