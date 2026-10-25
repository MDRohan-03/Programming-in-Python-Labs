
# Student Marks Investigator

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    if len(marks) == 0:
        return None

    total = 0

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

        total = total + mark

    return total / len(marks)



def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"



def display_report(students):
    for s in students:
        student_id = s[0]
        name = s[1]
        marks = s[2]

        average = calculate_average(marks)

        print("ID:", student_id)
        print("Name:", name)

        if average is None:
            print("Invalid or missing marks")
        else:
            print("Average:", round(average, 2))
            print("Performance:", classify_performance(average))



display_report(students)

print("Invalid mark test:")
print(calculate_average([80, 110, 90]))

print("Empty marks test:")
print(calculate_average([]))
