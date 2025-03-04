def print_odd_numbers(start, end):
    # Base case: if the start is greater than end, stop the recursion
    if start > end:
        return
    # Check if the current number is odd
    if start % 2 != 0:
        print(start)
    # Recursively call the function with the next number
    print_odd_numbers(start + 1, end)

    print_odd_numbers(1, 10)