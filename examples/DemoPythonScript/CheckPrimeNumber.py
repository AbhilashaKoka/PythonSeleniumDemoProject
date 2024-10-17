def is_Prime(number):
    if number<2:
        return False
        for i in range(2, int(number** 0.5)+1):
            if number % i==0:
                return False
                return True
num_to_check =29

if is_Prime(num_to_check):
    print(f"{num_to_check} is a prime number")
else:
    print(f"{num_to_check} is not a prime number")
