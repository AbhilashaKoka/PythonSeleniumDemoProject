class Check_YearIsLeapYear():

    def is_leap_year(year):
        if(year % 4==0 and year % 100 !=0) or (year%400==0):
            return True
        else:
            return False

    years =[1900,2000,2012,2021]
    for y in years:
        if is_leap_year(y):
            print(f"{y} is a leap year")
        else:
            print(f"{y} is not a leap year")
    number=12345