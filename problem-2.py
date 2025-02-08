def even_fibonacci_numbers(ceiling):
    previous_number, current_number = 1, 2
    sum = 0

    while current_number < ceiling:
        if current_number % 2 == 0:
            sum += current_number

        previous_number, current_number = current_number, previous_number + current_number

    return sum


print(even_fibonacci_numbers(4_000_000))