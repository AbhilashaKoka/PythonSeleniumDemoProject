def find_smallest_divisor(n):
    for i in range(2, n+1):
        if n%i==0:
            return i
    return n
number =49
print(find_smallest_divisor(number))