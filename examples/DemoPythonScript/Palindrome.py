

number = 12321

num_str = str(number)
is_palindrome_str = num_str == num_str[::-1]

reverse_number = 0
temp = number
while temp > 0:
    digit = temp % 10
    reverse_number = reverse_number * 10 + digit
    temp //= 10
is_palindrome_math=  number== reverse_number
print(f"String method {number} is a palindrome: {is_palindrome_str}")
print(f"Mathematical Method:The number {number} is a palindrome: {is_palindrome_math}")
