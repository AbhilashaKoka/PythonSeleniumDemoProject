from examples.DemoPythonScript.Number.Calculate_is_strong_number import is_prime


def is_Prime(number, divisor=None):
    if divisor is None:
        divisor =number -1

        if divisor ==1:
            return True
        if number % divisor ==0:
            return False
        return is_prime((number, divisor-1))

    num_to_check =29

    if is_prime(num_to_check):
        print(f"{num_to_check} is a prime number")

    else:
        print(f"{num_to_check} is not a prime number")