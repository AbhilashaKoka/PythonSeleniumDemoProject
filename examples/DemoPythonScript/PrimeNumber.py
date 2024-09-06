def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
     if num%i ==0:
         return False
    return True

def print_primes_in_range(start, end):
        for number in range(start, end +1):
            if is_prime(number):
                print(number)


start_range = 10
end_range = 50

print_primes_in_range(start_range, end_range)