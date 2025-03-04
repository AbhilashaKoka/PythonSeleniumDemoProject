class Check_Postive_Negative():

 def check_positive_negative(num):
    # Base case: if the number is greater than 0, it is positive
    if num > 0:
        return "Positive"
    # Base case: if the number is less than 0, it is negative
    elif num < 0:
        return "Negative"
    # Base case: if the number is 0, it is neither positive nor negative
    else:
        return "Neither Positive Nor Negative"

 print(check_positive_negative(10))
# Output: Positive
 print(check_positive_negative(-5))
# Output: Negative
 print(check_positive_negative(0))
# Output: Neither Positive Nor Negative