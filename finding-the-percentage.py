if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    student_marks = {}

    for _ in range(n):
        entry = input("Enter name and marks: ").split()
        name, *line = entry
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter name to query: ")
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
