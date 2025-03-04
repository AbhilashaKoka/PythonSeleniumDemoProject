class Armstrong_Number():

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