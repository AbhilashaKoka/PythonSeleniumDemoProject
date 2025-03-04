def calculate_grade(marks):
    total = sum(marks)
    average = total /len(marks)
    if average >= 90:
        grade = 'A'
    elif average >=80:
        grade ='B'
    elif average >=70:
        grade ='C'
    elif average >=60:
        grade = 'D'
    else:
        grade ='F'
    return total, average, grade

student_marks = [85,92,78,90,88]
total, average, grade = calculate_grade(student_marks)
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade : {grade}")
