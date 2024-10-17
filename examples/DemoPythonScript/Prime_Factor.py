def print_prime_factors(number):
    divisor =2
    while number >1:
        while number % divisor == 0:
            print(divisor,end='')
            number //=divisor
            divisor +=1
            print()

num_to_factor = 28
print_prime_factors(num_to_factor)