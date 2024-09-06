
def reverse_number(n):
    reverse_num =0
    while n>0:
        digit =n % 10
        reverse_num =reverse_num *10+digit
        n = n // 10
    return reverse_num

number =12345
print(reverse_number(number))