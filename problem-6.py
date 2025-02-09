def square_of_sum(ceiling):
    return sum(list(range(1, ceiling + 1))) ** 2

def sum_of_squares(ceiling):
    return sum([num ** 2 for num in range(1, ceiling + 1)])

print(square_of_sum(10))
print(sum_of_squares(10))

def sum_square_difference(ceiling):
    square_of_sum = sum(list(range(1, ceiling + 1))) ** 2
    sum_of_squares = sum([num ** 2 for num in range(1, ceiling + 1)])
    return square_of_sum - sum_of_squares

print(sum_square_difference(100))