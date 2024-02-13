num = int(input("Enter a number: "))
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))
result = sum_of_digits(num)

print("Sum of digits:", result)
