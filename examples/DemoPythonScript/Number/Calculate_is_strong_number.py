
def is_strong_number(number):
        str_number = str(number)
        sum_factorials =sum(factorial(int(digit)) for digit in str_number)
        return sum_factorials == number


