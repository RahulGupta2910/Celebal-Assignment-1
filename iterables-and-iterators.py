from itertools import combinations

def calculate_probability():
    n = int(input("Enter number of elements: "))
    letters = input("Enter the letters: ").lower().split()
    k = int(input("Enter number of indices: "))

    total = 0
    count = 0

    for combo in combinations(letters, k):
        total += 1
        if 'a' in combo:
            count += 1

    probability = count / total if total != 0 else 0
    print(f"{probability:.3f}")

calculate_probability()
