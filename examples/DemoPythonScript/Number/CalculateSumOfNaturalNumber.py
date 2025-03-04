def sum_of_natural_numbers(n):
    return n * (n+1) // 2
N=100
sum_of_numbers = sum_of_natural_numbers(N)
print(f"The sum of the first {N} natural numbers is :{sum_of_numbers}")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)