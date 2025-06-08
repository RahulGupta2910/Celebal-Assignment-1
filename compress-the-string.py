from itertools import groupby
s = input("Enter the string of numbers: ").strip()
if s.isdigit():
    for key, group in groupby(s):
        count = len(list(group))
        digit = int(key)
        print((count, digit), end=' ')
else:
    print("Invalid input. Please enter numbers only.")
