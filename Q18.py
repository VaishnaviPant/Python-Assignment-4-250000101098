def check_prime(n):
    if n <= 1:
        print("Not a prime number")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            return

    print("Prime number")

check_prime(17)