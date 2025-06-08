n = int(input("Enter the number of words: "))

counts = []
unique = []

print(f"Enter {n} words- ")

for _ in range(n):
    word = input().strip()
    if word not in unique:
        unique.append(word)
        counts.append(1)
    else:
        index = unique.index(word)
        counts[index] += 1

print(len(unique))

for count in counts:
    print(count, end=' ')
