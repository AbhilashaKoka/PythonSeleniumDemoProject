def print_number_recursively(start, end):
    print(start,end=' ')
    if start<end:
        print_number_recursively(start+1,end)

start_value = 1
end_value =10

print_number_recursively(start_value, end_value)