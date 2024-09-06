def reverse_number(n):
    reverse_num = 0
    while n > 0:
        digit = n % 10
        revered_num = reverse_num * 10 + digit
        n = n // 10
        return revered_num

number = 12345
print(reverse_number(number))
