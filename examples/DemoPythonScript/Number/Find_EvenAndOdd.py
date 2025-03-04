class Calculate_Even_And_Odd():

   def is_even_or_odd(num):
        # Base case for even
        if num == 0:
            return "Even"
        # Base case for odd
        elif num == 1:
            return "Odd"
        # Recursive step
        else:
        # Use the absolute value to handle negative numbers
         return Calculate_Even_And_Odd.is_even_or_odd(abs(num) - 1)



print(Calculate_Even_And_Odd.is_even_or_odd(10))
# Output: Even
# For an odd number
print(Calculate_Even_And_Odd.is_even_or_odd(11))
# Output: Odd
