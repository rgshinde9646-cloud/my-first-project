
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
    try:
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100.")
            break

        marks.append(mark)

    except ValueError:
        print("Error: Please enter a valid number.")
        break

if len(marks) == 3:
    average = sum(marks) / 3

    print("\nStudent:", name)
    print("Average:", round(average, 2))
    print("Grade:", calculate_grade(average))
