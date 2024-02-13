strings = ["one", "two", "three", "four", "five", "six"]
sorted_strings = sorted(strings, key=lambda x: (len(x), x))
print(sorted_strings)
