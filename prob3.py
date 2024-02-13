def find_max(numbers, compare):
    maximum = numbers[0]
    for num in numbers:
        if compare(num, maximum):
            maximum = num
    return maximum

numbers = [79, 1, 44, 78]
compare_func = lambda x, y: x > y
max_number = find_max(numbers, compare_func)
print(max_number)
