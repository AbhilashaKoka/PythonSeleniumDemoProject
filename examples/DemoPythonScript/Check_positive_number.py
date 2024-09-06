from tabnanny import check


def check_positive_negative(num):
    if(num>0):
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Negative Positive Nor Negative"

print(check_positive_negative(10))
print(check_positive_negative(-1))
print(check_positive_negative(0))