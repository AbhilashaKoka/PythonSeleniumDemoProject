class Check_NumberIsPalindrome():

    def is_palindrome_recursive(n, original_number=None):

        if original_number is None:
            original_number =n
        if n<10:
           return n==(original_number%10)
        if n%10 != original_number//(10**(len(str(n))-1)):
           return False
        n=(n%(10**(len(str(n))-1)))//10

        return is_palindrome_recursive(n, original_number //10)

    is_palindrome =is_palindrome_recursive(number)
    print(f"The number {number} is a palindrome: {is_palindrome}")