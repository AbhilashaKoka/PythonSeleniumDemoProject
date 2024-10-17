#Function to calculate the sum of proper divisors of a number
def sum_of_divisors(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div +=i
            return sum_div

#Function to check if two numbers are amicable
def are_amicable(num1, num2):
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

#number to be checked
num_a =220
num_b =284

if are_amicable(num_a, num_b):
    print(f"{num_a} and {num_b} are amicable numbers")
else:
    print(f"{num_a} and {num_b} are not amicable number.")
