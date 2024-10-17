def is_armstrong_number(number):

 str_num = str(number)

 num_digits = len(str_num)

 sum_of_digits = sum(int(digit) ** num_digits for digit in str_num)

 return sum_of_digits == number

num_to_check =153

if is_armstrong_number(num_to_check):
    print(f"{num_to_check} is an Armstrong number.")

else:
    print(f"{num_to_check} is not an Armstrong number.")


def check_positive_negative(num):
    if(num>0):
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Negative Positive Nor Negative"

print(check_positive_negative(10))
print(check_positive_negative(-1))
print(check_positive_negative(0))

def count_digits(n):
    count = 0
    while n>0:
        count +=1
        n //=10

    return count

number = 12345
digit_count =count_digits(number)
print(digit_count)

def find_largest(num1, num2, num3):
    if(num1>=num2) and (num1>=num3):
        largest = num1

    elif(num2>=num1) and (num2>=num3):
        largest =num2

    else:
        largest = num3

    return largest

number1 = 15
number2 = 27
number3 =12

largest_number = find_largest(number1, number2, number3)
print(f"The largest number among {number1}, {number2}, {number3} is: {largest_number}")

def is_leap_year(year):
    if(year % 4==0 and year % 100 !=0) or (year%400==0):
        return True
    else:
        return False

years =[1900,2000,2012,2021]
for y in years:
    if is_leap_year(y):
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not a leap year")

number=12345

def is_palindrome_recursive(n,original_number=None):
    if original_number is None:
        original_number =n

    if n<10:
        return n==(original_number%10)

    if n%10 != original_number//(10**(len(str(n))-1)):
        return False

    n=(n%(10**(len(str(n))-1)))//10
    return is_palindrome_recursive(n, original_number //10)

is_palindrome =is_palindrome_recursive(number)

print(f"The number {number} is a palindrome: {is_palindrome}")

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

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

def print_primes_in_range(start, end):
    for number in range(start, end +1):
        if is_prime(number):
            print(number)


start_range = 10
end_range = 50

print_primes_in_range(start_range, end_range)


def print_divisor(n):
    for i in range(1, n+1):
        if n%i==0:
            print(i)

number =28
print_divisor(number)

def print_table(number):

    for i in range(1,11):
        product =number * i
        print(f"{number}x {i}={product}")

num=5
print_table(num)

def reverse_number(n):
    reverse_num =0
    while n>0:
        digit =n % 10
        reverse_num =reverse_num *10+digit
        n = n // 10
    return reverse_num

number =12345
print(reverse_number(number))

def find_smallest_divisor(n):

    for i in range(2, n+1):

        if n%i==0:
            return i

    return n

number =49
print(find_smallest_divisor(number))




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

    def is_strong_number(number):
        str_number = str(number)
        sum_factorials =sum(factorial(int(digit)) for digit in str_number)
        return sum_factorials == number

def calculate_grade(marks):
    total = sum(marks)
    average = total /len(marks)
    if average >= 90:
        grade = 'A'
    elif average >=80:
        grade ='B'
    elif average >=70:
        grade ='C'
    elif average >=60:
        grade = 'D'
    else:
        grade ='F'

    return total, average, grade

student_marks = [85,92,78,90,88]
total, average, grade = calculate_grade(student_marks)

print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade : {grade}")