def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("\nStudent:", name)
print("Average:", round(average, 2))
print("Grade:", calculate_grade(average))
