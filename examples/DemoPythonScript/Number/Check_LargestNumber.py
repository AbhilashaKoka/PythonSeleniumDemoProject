
class Largest_Number():

 # Define the function to find the largest number among three
 def find_largest(num1, num2, num3):
    # Compare each number
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

 # Given numbers
 number1 = 15
 number2 = 27
 number3 = 12

 # Call the function to find the largest number
 largest_number = find_largest(number1, number2, number3)

 # Print the largest number
 print(f"The largest number among {number1}, {number2}, {number3} is: {largest_number}")