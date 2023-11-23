def float_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It's not a prime number")

# Your code above this line
n = int(input())
float_checker(number=n)