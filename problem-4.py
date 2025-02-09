def is_palindrome(number):
    return str(number) == str(number)[ : : -1]

def largest_palindrome(digit_number):
    ceiling = int(str(9) * digit_number)
    floor = int(str(9) * (digit_number - 1))

    largest_palindrome = 0

    for num1 in range(ceiling, floor, - 1):
        for num2 in range(num1, floor, - 1):
            product = num1 * num2

            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

print(largest_palindrome(3))