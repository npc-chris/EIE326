# GPA Calculator

def gpa_calculator():
    course = []
    grade = []
    course_grade_point = []

    grade_point_map = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2,
        "F": 0
    }

    for i in range(6):
        print("Count: ", i+1)
        course_name = input("Please enter the course name:\n")
        course.append(course_name)

        while True:
            g = input("Please enter your grade: (A, B, C, D, or F)\n").upper()
            if g in grade_point_map:
                grade.append(g)
                break
            else:
                print("Invalid grade. Please enter a valid grade (A, B, C, D, or F).")

        course_grade_point.append(grade_point_map[g])

    total_points = sum(course_grade_point)
    gpa = total_points / len(course_grade_point)

    print("\nYour GPA is:", round(gpa, 2))


gpa_calculator()
