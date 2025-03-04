class Reverse_Number():
   # Function to reverse a number
   def reverse_number(n):
    # Initialize the reversed number to 0
    reversed_num = 0
    # Loop until the number is greater than 0
    while n > 0:
        # Get the last digit of the number
        digit = n % 10
        # Add the digit to the reversed number's correct place
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the number
        n = n // 10
    # Return the reversed number
    return reversed_num

   # Number to be reversed
   number = 12345
   # Call the function and print the result
   print(reverse_number(number))