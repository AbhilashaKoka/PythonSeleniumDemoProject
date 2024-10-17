def find_duplicates(input_string):
    duplicates = {}
    for char in input_string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
    return {char: count for char, count in duplicates.items() if count > 1}

# Test the function
str = "Success"
result = find_duplicates(str)
print("Duplicate elements in the string:", result)

def reverse_number(n):

    reversed_num = 0

    while n > 0:

        digit = n % 10

        reversed_num = reversed_num * 10 + digit

        n = n // 10

    return reversed_num


number = 12345

print(reverse_number(number))