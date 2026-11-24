def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    print("Sum of digits:", total)

sum_digits(1234)