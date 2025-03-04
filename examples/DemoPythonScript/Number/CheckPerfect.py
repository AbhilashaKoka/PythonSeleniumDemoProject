def is_perfect_number(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
            return sum_of_divisors == number
num_to_check =28
if is_perfect_number(num_to_check):
    print(f"{num_to_check} is a perfect number.")
else:
    print(f"{num_to_check} is not a perfect number")


    # Function to check if a number is a perfect number
def is_perfect_number(number):
    # Initialize the sum of divisors
    sum_of_divisors = 0
    # Find the divisors of number
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    # Check if the sum of divisors is equal to the number
    return sum_of_divisors == number

# Number to be checked
num_to_check = 28
# Check if the number is a perfect number and print the result
if is_perfect_number(num_to_check):
    print(f"{num_to_check} is a perfect number.")
else:
    print(f"{num_to_check} is not a perfect number.")