def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

year = int(input("Enter the year you want to check: "))

if 1900 <= year <= 10**5:
    print(is_leap(year))
else:
    print("Input correct year")
