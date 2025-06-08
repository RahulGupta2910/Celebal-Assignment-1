def print_formatted(number):
    max_binary = bin(number)[2:]
    width = len(max_binary)

    for i in range(1, number + 1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]

        d = ' ' * (width - len(d)) + d
        o = ' ' * (width - len(o)) + o
        h = ' ' * (width - len(h)) + h
        b = ' ' * (width - len(b)) + b

        print(d, o, h, b)

n = int(input("Enter a number: "))
if(n>=1 and n<=99):
    print_formatted(n)
else:
    print("Give the number between the values 1 and 99.")
